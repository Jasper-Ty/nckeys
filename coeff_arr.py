from sage.all import *

class LabeledMatrix():


    def __init__(self, rows, cols):
        self.rows= rows
        self.cols = cols

        self.m = len(rows)
        self.n = len(cols)

        self.matrix = Matrix(ZZ, self.m, self.n)


    def __getitem__(self, key):
        row, col = key
        return self.matrix[self.rows[row], self.cols[col]]
    

    def __setitem__(self, key, val):
        row, col = key
        self.matrix[self.rows[row], self.cols[col]] = val


    def __mul__(self, right):
        if right.rows != self.cols:
            raise Exception("Wrong matrix sizes")
        product = LabeledMatrix(self.rows, right.cols)
        product.matrix = self.matrix * right.matrix
        return product
                    

    def table(self, colsize=3, rowsize=2, row_str=str, col_str=str, entry_str=str):

        width = self.n+1
        height = self.m+1
        lines = [[' ' for _ in  range(width)] for _ in range(height)]

        lines[0][0] = ' ' * colsize

        # draw row labels
        for row, i in self.rows.items():
            lines[i+1][0] = row_str(row).center(colsize)

        # draw col labels
        for col, j in self.cols.items():
            lines[0][j+1] = col_str(col).center(colsize)

        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                lines[i+1][j+1] = entry_str(val).center(colsize)
        
        return ('\n'*rowsize).join(''.join(line) for line in lines)
