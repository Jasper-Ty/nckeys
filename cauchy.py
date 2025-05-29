from sage.all import *

from lib import words, compositions, word_to_composition
from shapes import stairs
from labeled_matrix import LabeledMatrix


def h_biwords(squares, deg):
    raise NotImplementedError
    for subset in Subsets(squares, deg):
        for comp in compositions(deg, len(subset)):
            pass


def e_biwords(squares, deg):
    for subset in Subsets(squares, deg):
        lword = tuple(i for i,_ in subset)
        rword = tuple(j for _,j in subset)
        yield (lword, rword)

def invert_word(w, k):
    return tuple(k-n-1 for n in w)

def xu_triangle(deg, k):
    """
    Returns the coefficient array of the triangular Cauchy product
    where there are no relations among u and x commutes with everything
    """
    M = LabeledMatrix(words(deg, k), compositions(deg, k)) 

    squares = stairs(k)
    for lword, rword in e_biwords(squares, deg):
        x = word_to_composition(lword, k)
        u = invert_word(rword, k)
        M[u, x] += 1

    return M