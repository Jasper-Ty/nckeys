"""Module implementing the key basis.
"""

from ..core.cache import cache

from ..constants import *
from ..composition import Compositions
from ..operators import demazure
from ..matrix import Matrix, invert_unitriangular


@cache
def key_to_monomial(deg, n) -> Matrix:
    """
    Returns the matrix representing the transition matrix from the basis of
    key polynomials to the basis of monomials for the degree `deg` homogeneous
    component of the polynomial ring in `n` variables.
    """
    rows = Compositions(deg, n)
    cols = Compositions(deg, n)
    out = Matrix(
        rows, 
        cols,
        name=f"key{RIGHTARROW}{COMP_SYMB}", 
        rows_name=f"K(n: {n}, deg: {deg})",
        cols_name=f"{COMP_SYMB}(n: {n}, deg: {deg})",
    )

    for comp in Compositions(deg, n):
        s, w = comp.straighten()
        dem = demazure(w, deg=deg, n=n)
        for j in Compositions(deg, n):
            out[comp,j] = dem[s,j]
    
    return out


@cache
def monomial_to_key(deg, n) -> Matrix:
    out = invert_unitriangular(key_to_monomial(deg, n))
    out._name = f"{COMP_SYMB}{RIGHTARROW}key"
    out._rows_name = f"{COMP_SYMB}(n: {n}, deg: {deg})"
    out._cols_name = f"K(n: {n}, deg: {deg})"
    
    return out