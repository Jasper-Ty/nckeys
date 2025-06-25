from typing import Tuple

from .core.cache import cache

from .word import Word

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