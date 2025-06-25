"""
This file contains various utility and helper functions.
"""

from itertools import repeat
from typing import Tuple
from collections.abc import Sequence, Iterator

from .core.cache import cache

from .matrix import Matrix


def windows(seq: Sequence, length: int) -> Iterator[Tuple[tuple[int], tuple[int], tuple[int]]]:
    """All contiguous windows of `seq` of length `length`.
    """
    if length > len(seq) or length < 0:
            raise ValueError()

    return (
        (seq[:i], seq[i:i+length], seq[i+length:]) 
        for i in range(len(seq)-length+1)
    )


@cache
def straighten(seq: Sequence[int]) -> Tuple[tuple[int], tuple[int]]:
    """Sorts `seq` and returns the minimal length permutation that sorts it.
    Returns a pair `(s, rw)`, where `s` is `a` sorted in nonincreasing order,
    and `rw` is a reduced word of the permutation that takes `a` to `s`.

    (I believe this corresponds to the reduced word of the inverse of the 
    standardization of `a`?)
    """
    
    rw = []
    s = list(seq)

    while (ascents := list(filter(lambda i: s[i+1] > s[i], range(len(seq)-1)))):
        for ascent in ascents:
            s[ascent+1], s[ascent] = s[ascent], s[ascent+1]
            rw.append(ascent)

    rw.reverse()
    return (tuple(s), tuple(rw))


def subsequences_of_n(n: int, length: int) -> Iterator[tuple[int]]:
    """All subsequences of [0, ..., n-1] of length `length`
    """
    stack = [()]
    while stack:
        partial_subset = stack.pop()
        if len(partial_subset) == length:
            yield partial_subset
        else:
            i = partial_subset[-1] if partial_subset else -1
            stack.extend((*partial_subset, j) for j in reversed(range(i+1,n)))


def subsequences(seq: Sequence[int], length: int) -> Iterator[tuple[int]]:
    """All subsequences of `seq` of length `length`.
    """
    subseqs = subsequences_of_n(len(seq), length)
    return (tuple(map(seq.__getitem__, subseq)) for subseq in subseqs)


@cache
def sl2string(comp: Sequence[int], i: int, j: int) -> list[tuple[int]]:
    """Returns the sl2 string that `comp` generates.
    """
    if comp[i] == comp[j]:
        return [comp]

    if comp[i] > comp[j]:
        p, q = i, j
    else:
        p, q = j, i

    out = []

    base = list(comp)
    out.append(tuple(base))
    for m in range(comp[p]-comp[q]):
        base[p] -= 1
        base[q] += 1
        out.append(tuple(base))

    return out