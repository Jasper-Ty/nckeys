from sage.all import *
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base

from functools import cache

@cache
def divided_difference(i):
    """
    The `i`-th divided difference operator ∂ᵢ. 
    This function computes

                  f - sᵢf
                ─────────── .
                 xᵢ - xᵢ₊₁

    Where sᵢ acts by swapping xᵢ and xᵢ₊₁.
    """

    def op(p):
        assert isinstance(p.parent(), MPolynomialRing_base)
        x = (R := p.parent()).gens()
        assert i >= 0 and i < len(x)-1 , "Invalid operator"
        
        y = list(x)
        y[i], y[i+1] = y[i+1], y[i]

        return (
            (p - R.hom(y, R)(p))
            /(x[i]-x[i+1])
        ).numerator()

    op.__name__ = f"∂_{i}"
    
    return op

@cache
def demazure_operator(i):
    """
    The `i`-th Demazure operator πᵢ.
    This is defined by 
    
                πᵢ := ∂ᵢxᵢ
                
    """
    def op(p):
        assert isinstance(p.parent(), MPolynomialRing_base)
        x = p.parent().gens()
        assert i >= 0 and i < len(x)-1 , "Invalid operator"
        return divided_difference(i)(x[i]*p)

    op.__name__ = f"π_{i}"
        
    return op

@cache
def atom_operator(i):
    """
    The `i`-th 'atom' operator θᵢ.
    This is defined by 
    
                θᵢ(f) := ∂ᵢ - id
               
    """
    def op(p):
        assert isinstance(p.parent(), MPolynomialRing_base)
        return divided_difference(i)(p) - p

    op.__name__ = f"θ_{i}"
        
    return op

