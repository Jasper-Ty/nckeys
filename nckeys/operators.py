"""
This file defines divided difference, Demazure, and atom operators.
"""

from . import cache
from .matrix import Matrix
from .lib import compositions, sl2string
from .constants import *

@cache
def divided_difference(i, deg, n) -> Matrix:
    """
    Returns the linear map representing the `i`-th divided difference operator 
    ∂ᵢ restricted to the degree `deg` homogeneous component of the polynomial 
    ring in `n` variables.

    In general, the divided difference operator ∂ᵢ computes, for any function f,

                  f - sᵢf
                ─────────── .
                 xᵢ - xᵢ₊₁

    Where sᵢ acts by swapping xᵢ and xᵢ₊₁.
    """

    if i >= n-1 or i < 0 or deg <= 0:
        # deg = 0 shouldn't be an error (divided difference is well-defined on
        # constants--- it's the zero map), but I'm lazy to implement it
        raise IndexError

    rows = compositions(deg, n)
    cols = compositions(deg-1, n)
    out = Matrix(
        rows, 
        cols, 
        name=f"∂({i})",
        rows_name=f"{COMP_SYMB}(n: {n}, deg: {deg})",
        cols_name=f"{COMP_SYMB}(n: {n}, deg: {deg-1})"
    )

    for row in rows:
        deg_i = row[i]
        deg_j = row[i+1]

        if deg_i == deg_j:
            continue

        diminished = list(row)
        if deg_i > deg_j:
            diminished[i] -= 1
            sign = 1
        else:
            diminished[i+1] -= 1
            sign = -1
        diminished = tuple(diminished)

        for col in sl2string(diminished, i, i+1):
            out[row, col] = sign

    return out


@cache
def xmul(i, deg, n) -> Matrix:
    """
    Returns the linear map representing multiplication by xᵢ restricted to the 
    degree `deg` homogeneous component of the polynomial ring in `n` variables.
    """
    rows = compositions(deg, n)
    cols = compositions(deg+1, n)
    out = Matrix(
        rows, 
        cols, 
        name=f"x({i})",
        rows_name=f"{COMP_SYMB}(n: {n}, deg: {deg})",
        cols_name=f"{COMP_SYMB}(n: {n}, deg: {deg+1})"
    )

    for row in rows:
        col = list(row)
        col[i] += 1
        col = tuple(col)
        out[row, col] = 1

    return out


@cache
def demazure_operator(i, deg, n) -> Matrix:
    """
    Returns the linear map representing the `i`-th Demazure operator πᵢ 
    restricted to the degree `deg` homogeneous component of the polynomial ring 
    in `n` variables.

    In this case, we define the Demazure operator by the formula
    
                πᵢ := ∂ᵢxᵢ
                
    """
    dd = divided_difference(i, deg+1, n)
    x = xmul(i, deg, n)

    out = x * dd
    out._name = f"π({i})"
    return out


@cache
def demazure(*w, deg=3, n=6) -> Matrix:
    out = Matrix.identity(compositions(deg, n))

    for i in w:
        out *= demazure_operator(i, deg, n)

    out._name = f"π({', '.join(str(i) for i in w)})"
    out._rows_name = f"{COMP_SYMB}(n: {n}, deg: {deg})"
    out._cols_name = f"{COMP_SYMB}(n: {n}, deg: {deg})"
    
    return out


@cache
def atom_operator(i, deg, n):
    """
    Returns the linear map representing the `i`-th atom operator θᵢ restricted 
    to the degree `deg` homogeneous component of the polynomial ring in `n` 
    variables.

    We define the atom operator by the formula
    
                θᵢ := πᵢ - id
                
    """
    pass