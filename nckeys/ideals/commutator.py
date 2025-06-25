from ..core.cache import cache

from ..matrix import Matrix
from ..constants import *
from ..word import Words
from ..composition import Composition, Compositions

@cache
def words_to_compositions(deg, n):
    """
    Returns the quotient map sending words to compositions, i.e, the quotient
    map from a tensor power to a symmetric power.
    """
    rows = Words(deg, n)
    cols = Compositions(deg, n)

    out = Matrix(
        rows, 
        cols, 
        name=f"{WORD_SYMB}↠{COMP_SYMB}", 
        rows_name=f"{WORD_SYMB}(n: {n}, deg: {deg})",
        cols_name=f"{COMP_SYMB}(n: {n}, deg: {deg})",
        )

    for word in rows:
        comp = Composition.from_word(word, n)
        out[word, comp] += 1
    
    return out