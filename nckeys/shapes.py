"""
This file defines divided difference, Demazure, and atom operators.
"""

from itertools import chain
from nckeys import Matrix
from lib import subsets, words

def catalan(n: int):
    """
    """
    pass


def stairs(n: int):
    """
    (0,0) , ... , (0, n-1) , (1,0) , ... , (1,n-2) , ... , (n-1,0)
    """
    return list(chain.from_iterable(((i,j) for j in range(n-i)) for i in range(n)))


def rectangle(n: int):
    """
    (0,0) , ... , (0, n-1) , (1,0) , ... , (1,n-1) , ... , (n-1,n-1)
    """
    return list(chain.from_iterable(((i,j) for j in range(n)) for i in range(n)))


def biwords(shape, deg):
    """
    Returns all the biwords of a given shape
    """
    out = []
    for subset in subsets(shape, deg):
        left, right = zip(*subset)
        out.append((tuple(left), tuple(right)))

    return out


def size(shape):
    i_max = 0
    j_max = 0
    for i, j in shape:
        if i > i_max:
            i_max = i
        if j > j_max:
            j_max = j
    return (i_max + 1, j_max + 1)


def word_matrix(shape, deg):
    """
    Returns the matrix of words for a given shape
    """
    i_dim, j_dim = size(shape)
    rows = words(deg, i_dim)
    cols = words(deg, j_dim)
    out = Matrix(
        rows, 
        cols, 
        name=f"{deg}-words",
        rows_name=f"Words(n: {i_dim}, deg: {deg})",
        cols_name=f"Words(n: {j_dim}, deg: {deg})",
    )
    for left, right in biwords(shape, deg):
        out[left, right] += 1
    
    return out