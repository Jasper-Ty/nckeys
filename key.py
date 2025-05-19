from sage.all import *

from functools import cache

from lib import straighten, compositions, monomial_vector
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
def key_to_monomial_matrix(d: int, n: int):
    """
    Returns the transition matrix from the key basis to the monomial basis for the
    degree `d` component of the polynomial ring in `n` variables.
    """
    return matrix(
        [
            monomial_vector(key_polynomial(w)) 
            for w in compositions(d, num_parts=n)
        ],
        immutable=True
    )


@cache
def monomial_to_key_matrix(d: int, n: int):
    """
    Returns the transition matrix from the monomial basis to the key basis for the
    degree `d` component of the polynomial ring in `n` variables.
    """
    return key_to_monomial_matrix(d,n).inverse()