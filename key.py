from sage.all import *

from functools import cache

from lib import straighten, compositions
from operators import demazure_operator


def key_polynomial(a: tuple[int], var='x'):
    """
    The key polynomial indexed by `a`
    """
    s, rw = straighten(a)
    R = PolynomialRing(ZZ, var, len(s))

    # Apply sequence of Demazure operators to the highest weight
    return reduce(
        lambda f, i: demazure_operator(i)(f),
        rw,
        R.monomial(*s)
    )


@cache
def monomial_vector(f, deg, k):
    """
    Returns the coefficients of a homogeneous polynomial indexed by
    compositions (exponent vectors) in lex order.
    """
    return vector(
        f[mon] 
        for mon in compositions(deg, k)
    )


from labeled_matrix import LabeledMatrix

@cache
def key_to_monomial_matrix(deg: int, k: int):
    """
    Returns the transition matrix from the key basis to the monomial basis for the
    degree `d` component of the polynomial ring in `n` variables.
    """
    out = LabeledMatrix(compositions(deg, k), compositions(deg, k))
    vectors = [
            monomial_vector(key_polynomial(w), deg, k) 
            for w in compositions(deg, k)
    ]
    out.matrix = matrix(
        vectors,
        immutable=True
    )
    return out


@cache
def monomial_to_key_matrix(deg: int, k: int):
    """
    Returns the transition matrix from the monomial basis to the key basis for the
    degree `d` component of the polynomial ring in `n` variables.
    """
    out = key_to_monomial_matrix(deg,k)
    out.matrix = out.matrix.inverse()
    return out