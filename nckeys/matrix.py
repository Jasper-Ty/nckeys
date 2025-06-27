"""
Implementation of matrices with labeled rows and columns.

Linear algebra capabilities are minimal.
"""
import scipy


class Matrix:
    """An integer matrix class with arbitrary row and column indices.
    """
    def __init__(self, rows, cols, name=None, rows_name=None, cols_name=None):
        self._data = dict()

        self._rows = rows.copy()
        self._cols = cols.copy()
        self._name = name
        self._rows_name = rows_name
        self._cols_name = cols_name

        for row in rows:
            for col in cols:
                self._data[(row, col)] = 0

    
    def transpose(self):
        out = Matrix(self.cols, self.rows, name=f"({self._name})ᵀ")
        out._cols_name = self._rows_name
        out._rows_name = self._cols_name
        
        for row in self._rows:
            for col in self._cols:
                out[col, row] = self[row, col]
            
        return out


    def submatrix(self, rows=None, cols=None):
        pass
    

    def identity(rows):
        out = Matrix(rows, rows)
        for row in rows:
            out[(row, row)] = 1
        out._name = "id"
        return out
    

    def clone(self) -> "Matrix":
        out = Matrix(
            self._rows,
            self._cols,
            name=self._name,
            rows_name=self._rows_name,
            cols_name=self._cols_name
        )

        for i in self._rows:
            for j in self._rows:
                out[i,j] = self[i,j]

        return out


    def set(self, row, col, val):
        if (row, col) not in self:
            raise KeyError(f"Index ({row}, {col}) does not exist in matrix.")
        self._data[(row, col)] = val

    
    def get(self, row, col):
        if (row, col) not in self:
            raise KeyError(f"Index ({row}, {col}) does not exist in matrix.")
        return self._data[(row, col)]


    def __getitem__(self, key):
        row, col = key
        return self.get(row, col)

    
    def __setitem__(self, key, val):
        row, col = key
        return self.set(row, col, val)

    
    def __contains__(self, key):
        row, col = key
        return row in self._rows and col in self._cols


    @property
    def rows(self):
        return self._rows.copy()

    
    @property
    def cols(self):
        return self._cols.copy()


    def row(self, row):
        for col in self.cols:
            yield self[row, col]

    
    def col(self, col):
        for row in self.rows:
            yield self[row, col]


    @property
    def nrows(self) -> int:
        return len(self._rows)
    

    @property
    def ncols(self) -> int:
        return len(self._cols)


    def is_square(self):
        return self.nrows == self.ncols

    
    def keys(self):
        return iter(self._data.keys())

    
    def is_nonnegative(self):
        return all(x >= 0 for x in self._data.values())


    def __eq__(self, right):
        if self.rows != right.rows:
            return False
        if self.cols != right.cols:
            return False

        for row in self._rows:
            for col in self._cols:
                if self[row, col] != right[row, col]:
                    return False

        return True

    
    def __add__(self, right) -> "Matrix":
        if self._cols != right._cols or self._rows != right._rows:
            raise KeyError("Incompatible matrix addition")
        
        out = self.clone()
        out._name = f"{self._name} + {right._name}"

        for i in self._rows:
            for j in self._cols:
                out[i, j] += right[i, j]
        
        return out

    
    def __neg__(self) -> "Matrix":
        out = self.clone()
        out._name = f"-{self._name}"

        for i in self._rows:
            for j in self._cols:
                out[i, j] = -out[i, j]
        
        return out
    

    def __sub__(self, right) -> "Matrix":
        if self._cols != right._cols or self._rows != right._rows:
            raise KeyError("Incompatible matrix addition")
        
        out = self + (-right)
        out._name = f"{self._name} - {right._name}"

        return out


    def __mul__(self, right) -> "Matrix":
        if self._cols != right._rows:
            raise KeyError("Incompatible matrix multiplication")

        out = Matrix(self._rows, right._cols)
        out._name = f"{self._name} × {right._name}"
        out._rows_name = self._rows_name
        out._cols_name = right._cols_name

        for i in self._rows:
            for j in right._cols:
                for k in self._cols:
                    out[i, j] += self[i, k] * right[k, j]
        
        return out

    
    def __pow__(self, exponent) -> "Matrix":
        if not (isinstance(exponent, int) and exponent >= 0):
            raise ValueError("Can't raise matrix to non integer exponent")

        out = Matrix.identity(self._rows)

        for _ in range(exponent):
            out *= self

        out._name = f"{self._name}^{exponent}"

        return out


    def __repr__(self) -> str:
        """String representation."""
        return f"Matrix({self._rows}, {self._cols})"


    def __str__(self):
        """Pretty string representation of the matrix."""
        row_label_width = max(len(str(row)) for row in self._rows)
        col_widths = [max(max(len(str(row)) for row in self.col(col)), len(str(col))) for col in self._cols]
        total_width = 1 + (row_label_width + 2) + sum((width+3) for width in col_widths) + 1

        top = "╭" + "─" * (row_label_width+2) + "┬" + "┬".join("─" * (width+2) for width in col_widths) + "╮\n"
        bar = "├" + "─" * (row_label_width+2) + "┼" + "┴".join("─" * (width+2) for width in col_widths) + "┤\n"
        mid = "├" + "─" * (row_label_width+2) + "┤" + "·".join(f" {'·':^{width}} " for width in col_widths) + "│\n"
        bot = "╰" + "─" * (row_label_width+2) + "┴" + "─".join("─" * (width+2) for width in col_widths) + "╯"

        out = ""
        if self._name is not None:
            out += f"{self._name:^{total_width}}\n"
        if self._rows_name is not None and self._cols_name is not None:
            s = f"rows: {self._rows_name}  cols: {self._cols_name}"
            out += f"{s:^{total_width}}\n"
        out += top 
        out += "│" + " " * (row_label_width+2) + "│" + "│".join(f" {str(col):^{col_width}} " for col, col_width in zip(self._cols, col_widths)) + "│\n"
        out += bar

        rows = self._rows
        for i in range(len(rows)):
            row = rows[i]
            entries = self.row(row)
            out += "│" + f" {str(row):^{row_label_width}} " + "│" + "·".join(f" {str(entry) if entry != 0 else '':^{col_width}} " for entry, col_width in zip(entries, col_widths)) + "│\n"
            if i < len(rows) - 1:
                out += mid
            else:
                out += bot

        return out


def row_swap(row_a, row_b, rows):
    """
    Constructs the elementary matrix which swaps two rows
    """
    out = Matrix(rows, rows, name=f"{row_a} ↔ {row_b}")

    for row in rows:

        if row == row_a:
            out[(row, row_b)] = 1
        elif row == row_b:
            out[(row, row_a)] = 1
        else:
            out[(row, row)] = 1

    return out


def row_scale(row, scale, rows):
    """
    Constructs the elementary matrix which scales a row
    """
    out = Matrix.identity(rows)
    out[(row, row)] *= scale

    return out


def row_sum(row_a, row_b, rows):
    """
    Constructs the elementary matrix which sums two rows
    """
    out = Matrix(rows, rows, name=f"{row_a} ← {row_a} + {row_b}")

    for row in rows:
        out[(row, row)] = 1
        if row == row_a:
            out[(row, row_b)] = 1

    return out


def invert_unitriangular(A) -> Matrix:
    """Inverts a unitriangular matrix A via a geometric sum expansion
    """

    I = Matrix.identity(A.rows)
    N = I - A
    out = sum((N**i for i in range(A.nrows)), start=Matrix(A.rows, A.rows))
    out._name = f"({A._name})^-1"

    return out

