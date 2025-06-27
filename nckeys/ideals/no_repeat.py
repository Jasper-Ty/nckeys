from itertools import chain

from ..core.cache import cache

from ..matrix import Matrix
from ..constants import *
from ..word import Word, Words, permutations
from ..composition import Composition, Compositions
from ..lib import subsequences_of_n

@cache
def no_repeat(deg, n):
    """
    """
    rows = Words(deg, n)
    cols = [Word(*map(seq.__getitem__, p)) for p in permutations(deg) for seq in subsequences_of_n(n, deg)]
    
    out = Matrix(
        rows, 
        cols, 
        name=f"{WORD_SYMB}↠{COMP_SYMB}", 
        rows_name=f"{WORD_SYMB}(n: {n}, deg: {deg})",
        cols_name=f"{WORD_SYMB}'(n: {n}, deg: {deg})",
        )

    for word in cols:
        out[word, word] += 1
    
    return out