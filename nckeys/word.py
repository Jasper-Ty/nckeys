"""
A word is defined to be a tuple of nonnegative integers
"""

from typing import Union
from itertools import chain

from .core.cache import cache

from .lib import straighten, windows


class Word(tuple):
    """
    A tuple of nonnegative integers.
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
        return max(self, default=-1) + 1


    def straighten(self):
        s, rw = straighten(self)
        return Word(*s), Word(*rw)


    def windows(self, length):
        return windows(self, length)


    def matches(self, *patterns):
        for pattern in patterns:
            if len(pattern) > len(self):
                continue
            for prefix, subword, suffix in self.windows(len(pattern)):
                if subword == pattern:
                    yield (prefix, subword, suffix) 

    
    def rewrites(self, lword, rword):
        """ All possible applications of the rule `lword -> rword`. 
        """
        for prefix, _, suffix in self.matches(lword):
            yield prefix + rword + suffix
    

    def is_partition(self):
        return all(self[i] >= self[i+1] for i in range(self.deg-1))
    

    def __getitem__(self, key):
        result = super().__getitem__(key)
        if isinstance(key, slice):
            return Word(*result)
        return result

    
    def __add__(self, other):
        return Word(*super().__add__(other))


    def __str__(self):
        return f"[{', '.join(map(str, self))}]"


@cache
def Words(deg, n) -> list[Word]:
    """
    Returns a list of all words of length `deg` in the letters `0, ..., n-1`, 
    in reverse lex order.
    """
    return [
        Word(i, *rest)
        for i in reversed(range(n))
        for rest in Words(deg-1, n)
    ] if deg > 0 else [Word()]


@cache
def permutations(n: int) -> list[Word]:
    """Returns a list of all permutations of `n` in reverse lex order
    """
    return [
        p[:i] + Word(n-1) + p[i:]
        for i in range(n)
        for p in permutations(n-1)
    ] if n > 0 else [Word()]


@cache
def partitions(n: int, m=None) -> list[Word]:
    """
    """
    m = n if m is None else m
    return [
        Word(i, *rest)
        for i in range(1, m+1)
        for rest in partitions(n-i, m=i)
    ] if n > 0 else [Word()]