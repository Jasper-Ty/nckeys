"""Provides classes and methods for working with integer compositions.
"""

from typing import Union

from itertools import repeat

from .core.cache import cache
from .lib import straighten, sl2string
from .word import Word


class Composition(tuple):
    """A tuple of nonnegative integers.
    """

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

    
    def sl2string(self, i, j):
        return [Composition(*tup) for tup in sl2string(self, i, j)]


    def from_word(w,n=None):
        n = w.n if n is None else n
        c = [0] * n
        for i in w:
            c[i] += 1
        return Composition(*c)


    def __str__(self):
        return f"({', '.join(map(str, self))})"


@cache
def Compositions(deg, n) -> list[Composition]:
    """
    Returns a list of all nonnegative integer compositions of degree `deg`
    with `n` parts, in reverse lex order.
    """
    return [
        Composition(deg-i, *rest)
        for i in range(deg+1) 
        for rest in Compositions(i,n-1) 
    ] if deg > 0 and n > 1 else [Composition(deg, *repeat(0, n-1))]