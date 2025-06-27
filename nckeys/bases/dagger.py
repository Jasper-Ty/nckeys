

from ..core.cache import cache

from ..constants import *
from ..word import Word, Words
from ..matrix import Matrix

@cache
def dagger_matrix(deg, n) -> Matrix:
    rows = Words(deg, n)
    cols = Words(deg, n)
    out = Matrix(
        rows, 
        cols,
        name=f"†", 
        rows_name=f"{WORD_SYMB}(n: {n}, deg: {deg})",
        cols_name=f"{WORD_SYMB}(n: {n}, deg: {deg})",
    )

    for word in Words(deg, n):
        flipped = Word(*(n-i-1 for i in word))
        out[word, flipped] = 1

    return out