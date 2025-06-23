"""
Utility functions
"""

from itertools import repeat
from typing import Tuple

from .matrix import Matrix
from . import cache


@cache
def straighten(a: tuple[int]) -> Tuple[tuple[int], tuple[int]]:
    """
    Returns a pair `(s, rw)`, where `s` is `a` sorted in nonincreasing order,
    and `rw` is a reduced word of the permutation that takes `a` to `s`.
    """
    
    rw = []
    s = list(a)

    while (ascents := list(filter(lambda i: s[i+1] > s[i], range(len(a)-1)))):
        for ascent in ascents:
            s[ascent+1], s[ascent] = s[ascent], s[ascent+1]
            rw.append(ascent)

    rw.reverse()
    return (tuple(s), tuple(rw))


@cache
def compositions(deg, k):
    """
    Returns a list of all nonnegative integer compositions of degree `deg`
    with `k` parts, in reverse lex order.
    """
    return [
        (deg-i, *rest)
        for i in range(deg+1) 
        for rest in compositions(i,k-1) 
    ] if deg > 0 and k > 1 else [(deg, *repeat(0, k-1))]


@cache
def words(deg, k):
    """
    Returns a list of all words of length `deg` on `k` letters, in reverse lex order
    """
    return [
        (i, *rest)
        for i in reversed(range(k))
        for rest in words(deg-1, k)
    ] if deg else [()]


@cache
def word_to_composition(w,n=None):
    n = max(w) + 1 if n is None else n
    c = [0] * n
    for i in w:
        c[i] += 1
    return tuple(c)


@cache
def _subsets(n, deg):
    """
    Returns all subsets of [`n`] of size `deg`
    """
    subsets = []
    stack = [[]]
    while stack:
        partial_subset = stack.pop()
        if len(partial_subset) == deg:
            subsets.append(partial_subset)
        else:
            i = partial_subset[-1] + 1 if partial_subset else 0
            for j in reversed(range(i,n)):
                new_subset = partial_subset.copy()
                new_subset.append(j)
                stack.append(new_subset)
   
    return subsets


def subsets(arr, deg):
    """
    Returns all subsets of `arr` of size `deg`
    """
    return [[arr[i] for i in index_subset] for index_subset in _subsets(len(arr), deg)]


@cache
def sl2string(comp, i, j):
    """
    Returns the smallest sl2 string that `comp` has to be contained in
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