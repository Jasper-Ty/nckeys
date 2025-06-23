"""
A word is defined to be a tuple of nonnegative integers
"""

from typing import Union

from . import cache
from .lib import straighten


class Word(tuple):
    """
    A tuple of nonnegative integers.
    The collection of words will be referred to as 𝕨. 
    """
    def __new__(cls, *W):
        if not all(isinstance(w, int) and w >= 0 for w in W):
            raise ValueError("Trying to build word with non-nonnegative integers")
        return super(Word, cls).__new__(cls, tuple(W))


    @property
    def deg(self) -> int:
        """
        The degree of the word as a noncommutative monomial, i.e, its length as 
        a string.
        """
        return len(self)


    @property 
    def n(self) -> int:
        """
        The number of distinct letters appearing in a word.
        """
        return max(self, default=0)


    def straighten(self):
        """
        Returns a pair `(s, rw)`, where `s` is `self` sorted in nonincreasing 
        order, and `rw` is a reduced word of the shortest permutation that takes 
        `self` to `s`.

        (I believe this corresponds to the reduced word of the standardization 
        of `self`?)
        """
        s, rw = straighten(self)
        return Word(*s), Word(*rw)


    def __str__(self):
        return f"[{', '.join(map(str, self))}]"


@cache
def Words(deg, k) -> list[Word]:
    """
    Returns a list of all words of length `deg` on `k` letters, in reverse lex 
    order.
    """
    return [
        Word(i, *rest)
        for i in reversed(range(k))
        for rest in Words(deg-1, k)
    ] if deg > 0 else [Word()]