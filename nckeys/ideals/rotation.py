from typing import Tuple

from ..core.cache import cache
from ..constants import *

from ..word import Word
from ..bijectivization import Bijectivization


@cache
def RkRelations(n, k):

    acb_cab = [
        (Word(a,c,b), Word(c,a,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a > k
    ]
    bca_bac = [
        (Word(b,c,a), Word(b,a,c)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a > k
    ]
    far_knuth = acb_cab + bca_bac

    bac_acb = [
        (Word(b,a,c), Word(a,c,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a <= k
    ]
    bca_cab = [
        (Word(b,c,a), Word(c,a,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a <= k
    ]
    near_rotation = bac_acb + bca_cab

    aa = [
        (Word(a,a), None) 
        for a in range(n)
    ]

    aba = [
        (Word(a,b,a), None) 
        for a in range(n) for b in range(n) 
    ]

    return far_knuth + near_rotation + aa + aba


@cache
def rk_quotient(deg, n, k):
    I = Bijectivization(RkRelations(n, k))
    out = I.quotient(deg, n)
    out._name = f"r{k}"
    out._rows_name =f"{WORD_SYMB}(deg: {deg}, n: {n})"
    out._cols_name =f"R_k^⟂(deg: {deg+1}, n: {n})"

    return out