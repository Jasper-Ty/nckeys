"""
A word is defined to be a tuple of nonnegative integers
"""

from typing import Union

from itertools import repeat

from . import cache
from .lib import straighten
from .word import Word


class Composition(tuple):
    def __new__(cls, *W):
        if not all(isinstance(w, int) and w >= 0 for w in W):
            raise ValueError("Trying to build composition with non-nonnegative integers")
        return super(Composition, cls).__new__(cls, tuple(W))


    @property
    def deg(self) -> int:
        return sum(self)


    @property 
    def n(self) -> int:
        return len(self)


    def straighten(self):
        s, rw = straighten(self)
        return Composition(*s), Word(*rw)


    def __str__(self):
        return f"({', '.join(map(str, self))})"


@cache
def Compositions(deg, n) -> list[Composition]:
    """
    Returns a list of all nonnegative integer compositions of degree `deg`
    with `k` parts, in reverse lex order.
    """
    return [
        Composition(deg-i, *rest)
        for i in range(deg+1) 
        for rest in Compositions(i,n-1) 
    ] if deg > 0 and n > 1 else [Composition(deg, *repeat(0, n-1))]