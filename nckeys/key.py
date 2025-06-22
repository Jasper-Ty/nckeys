"""
This module implements key polynomials, packaged as transition matrices with 
columns labeled by monomials and rows labeled by keys
"""

from . import cache
from .constants import *
from .lib import compositions, straighten
from .operators import demazure
from .matrix import Matrix, invert_unitriangular


@cache
def key_to_monomial(deg, n) -> Matrix:
    rows = compositions(deg, n)
    cols = compositions(deg, n)
    out = Matrix(
        rows, 
        cols,
        name=f"key{RIGHTARROW}monomial", 
        rows_name=f"K(n: {n}, deg: {deg})",
        cols_name=f"{COMP_SYMB}(n: {n}, deg: {deg})",
    )

    for i in compositions(deg, n):
        s, w = straighten(i)
        dem = demazure(*w, deg=deg, n=n)
        for j in compositions(deg, n):
            out[i,j] = dem[s,j]
    
    return out


@cache
def monomial_to_key(deg, n) -> Matrix:
    out = invert_unitriangular(key_to_monomial(deg, n))
    out._name = f"monomial{RIGHTARROW}key"
    out._rows_name = f"{COMP_SYMB}(n: {n}, deg: {deg})"
    out._cols_name = f"K(n: {n}, deg: {deg})"
    
    return out