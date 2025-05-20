from sage.all import *

from itertools import chain

from lib import words, compositions

def stairs(n: int):
    """
    (0,0) , ... , (0, n-1) , (1,0) , ... , (1,n-2) , ... , (n-1,0)
    """
    return chain.from_iterable(((i,j) for j in range(n-i)) for i in range(n))

# need: 
# - arbitrary shape (easy)
# - arbitrary indices (!)
#   - algorithm to turn words into elements

def stairs_coeff_arr(degree: int, n: int):
    """
    Returns the coefficient array
    """
    idx_x = compositions(degree, num_parts=n)
    idx_u = words(length=degree, num_letters=n)

    x_idx = { comp: i for i, comp in enumerate(idx_x) }
    u_idx = { word: i for i, word in enumerate(idx_u) }

    M = matrix(ZZ, len(idx_u), len(idx_x))

    squares = stairs(n)
    for subset in Subsets(squares, k=degree):
        x = [0] * n 
        u = []
        for i,j in subset:
            x[i] += 1
            u.append(n-j-1)
        
        x, u = tuple(x), tuple(u)
        M[u_idx[u], x_idx[x]] += 1
    
    return M

def wc_table(matrix, degree: int, n: int):
    C = compositions(degree, num_parts=n)
    W = words(length=degree, num_letters=n)

    rowheight = 1
    colwidth = n+2

    nc = len(C)
    nw = len(W)

    width = nc + 2
    height = nw + 2
    lines = [[' ' for _ in  range(width)] for _ in range(height)]

    lines[0][0] = ' ' * colwidth 
    for x in range(width):
        lines[1][x] = '─' * colwidth
    for y in range(height):
        lines[y][1] = '│'.center(colwidth)
    lines[1][1] = '┼'.center(colwidth, '─')
    
    for i, w in enumerate(W):
        lines[i+2][0] = ''.join(str(n) for n in w).center(colwidth)
    
    for j, c in enumerate(C):
        lines[0][j+2] = ''.join(str(n) for n in c).center(colwidth)

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            s = f"{val}" if val else " "
            lines[i+2][j+2] = s.center(colwidth)
    
    return ('\n'*rowheight).join(''.join(line) for line in lines)