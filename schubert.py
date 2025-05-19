from sage.all import *

from operators import divided_difference 

def schubert(w: tuple[int], var='x'):
    """
    The Schubert polynomial indexed by `w`
    """
    n = max(w) + 2
    return reduce(
        lambda f, i: divided_difference(i)(f), 
        w, 
        PolynomialRing(ZZ, var, n).monomial(*reversed(range(n)))
    )