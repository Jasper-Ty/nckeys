from sage.all import *

from lib import straighten
from operators import demazure_operator

def key_polynomial(a: tuple[int], var='x'):
    """
    The key polynomial indexed by `a`
    """
    s, rw = straighten(a)
    R = PolynomialRing(ZZ, var, len(s))
    return reduce(
        lambda f, i: demazure_operator(i)(f),
        rw,
        R.monomial(*s)
    )

print(key_polynomial((0,1,2)))

