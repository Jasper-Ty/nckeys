from sage.all import *

from lib import straighten
from operators import atom_operator 

def atom(a, var='x'):
    """
    The Demazure atom indexed by `a`
    """
    s, rw = straighten(a)
    R = PolynomialRing(ZZ, var, len(a))
    return reduce(
        lambda f, i: atom_operator(i)(f), 
        rw, 
        R.monomial(*s)
    )