from itertools import chain

from .core.cache import cache
from .constants import *
from .matrix import Matrix
from .lib import subsequences
from .word import Word, Words
from .composition import Compositions
from .bases import dagger_matrix

def diagram(w, rev=False):
    """
    """
    if rev:
        return list(
            chain.from_iterable(
                ((i,j) for j in reversed(range(w_i))) 
                for i, w_i in enumerate(w)
                )
            )
    else:
        return list(
            chain.from_iterable(
                ((i,j) for j in range(w_i)) 
                for i, w_i in enumerate(w)
                )
            )


def partition_nonsymm(n: int):
    """
    """
    pass


@cache
def stairs(n: int):
    """
    (0,0) , ... , (0, n-1) , (1,0) , ... , (1,n-2) , ... , (n-1,0)
    """
    return list(chain.from_iterable(((i,j) for j in range(n-i)) for i in range(n)))


@cache
def stairs_nonsymm(n: int):
    """
    (0,n-1) , ... , (0, 0) , (1,n-1) , ... , (1,1) , ... , (n-1,n-1)
    """
    return list(chain.from_iterable(((i,j) for j in range(n-i)) for i in range(n)))


def rectangle(n: int):
    """
    (0,0) , ... , (0, n-1) , (1,0) , ... , (1,n-1) , ... , (n-1,n-1)
    """
    return list(chain.from_iterable(((i,j) for j in range(n)) for i in range(n)))


def e_biwords(shape, deg):
    """
    Returns all the biwords of a given shape
    """
    out = []
    for subsequence in subsequences(shape, deg):
        left, right = zip(*subsequence)
        out.append((Word(*left), Word(*right)))

    return out


def h_biwords(shape, deg):
    """
    Returns all the biwords of a given shape
    """
    out = []
    m = len(shape)
    for comp in Compositions(deg, m):
        left = []
        right = []

        for (x, y), c in zip(shape, comp):
            left += [x] * c
            right += [y] * c
        
        out.append((Word(*left), Word(*right)))

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


def biword_matrix(shape, deg, expansion="h", dagger=False):
    """Returns the matrix of words for a given shape
    """
    i_dim, j_dim = size(shape)
    
    rows = Words(deg, i_dim)
    cols = Words(deg, j_dim)
    out = Matrix(
        rows, 
        cols, 
        rows_name=f"{WORD_SYMB}(n: {i_dim}, deg: {deg})",
        cols_name=f"{WORD_SYMB}(n: {j_dim}, deg: {deg})",
    )
 
    if expansion == "h":
        biwords = h_biwords(shape, deg)
    elif expansion == "e":
        biwords = e_biwords(shape, deg) 

    for left, right in biwords:
        out[left, right] += 1

    if (dagger and expansion == "h") or (not dagger and expansion == "e"):
            out = out * dagger_matrix(deg, j_dim)
    
    return out


@cache
def root_ideals(n):
    if n == 0:
        return [[]]

    out = []
    for p in range(n):
        q = n-p-1
        for A in root_ideals(q):
            for B in root_ideals(p):
                partition = Word(*(A[i] + p for i in range(q)), p, *B)
                out.append(partition)

    return out