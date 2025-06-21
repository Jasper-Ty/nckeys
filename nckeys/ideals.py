from functools import cache

from .lib import words, compositions, word_to_composition
from .matrix import Matrix
from .constants import *

@cache
def commutator_quotient_map(deg, n):
    """
    Returns the quotient map sending words to compositions, i.e, the quotient
    map from a tensor power to a symmetric power.
    """
    rows = words(deg, n)
    cols = compositions(deg, n)

    out = Matrix(
        rows, 
        cols, 
        name=f"{WORD_SYMB}→{COMP_SYMB}(n: {n}, deg: {deg})", 
        rows_name=f"{COMP_SYMB}(n: {n}, deg: {deg})",
        cols_name=f"{WORD_SYMB}(n: {n}, deg: {deg})",
        )

    for word in rows:
        comp = word_to_composition(word, n)
        out[word, comp] += 1
    
    return out


def plactic_quotient_map(deg, n):
    """
    Returns the quotient map sending words to plactic equivalence classes,
    which are tableaux
    """
    pass


def rotation_quotient_map(k, deg, n):
    """
    Returns the quotient map sending words to I_{R,k} equivalence classes
    """
    pass