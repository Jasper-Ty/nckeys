from typing import Tuple

from ..core.cache import cache
from ..constants import *

from ..word import Word
from ..tableau import tableau_word
from ..bijectivization import Bijectivization


@cache
def plactic_relations(n: int) -> list[Tuple[Word, Word]]:
    aba_baa = [
        (Word(a,b,a), Word(b,a,a)) 
        for a in range(n) for b in range(n) 
        if a < b
    ]
    bab_bba = [
        (Word(b,a,b), Word(b,b,a)) 
        for a in range(n) for b in range(n) 
        if a < b
    ]
    acb_cab = [
        (Word(a,c,b), Word(c,a,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c
    ]
    bca_bac = [
        (Word(b,c,a), Word(b,a,c)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c
    ]
    return aba_baa + bab_bba + acb_cab + bca_bac


@cache
def plactic_quotient(deg, n):
    I = Bijectivization(
        plactic_relations(n), 
        representative=lambda s: tableau_word(next(iter(s)))
    )
    w2t = I.quotient(deg, n)
    w2t._name = "plac"
    w2t._rows_name=f"{WORD_SYMB}(deg: {deg}, n: {n})",
    w2t._cols_name=f"T(deg: {deg+1}, n: {n})"

    return w2t