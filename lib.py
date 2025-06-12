from sage.all import *

from functools import cache
from itertools import repeat
from bidict import bidict

id = lambda x: x

def compose(*funcs, reverse=False):
    funcs = list(funcs)
    if reverse:
        funcs.reverse()
    def composed(*args, **kwargs):
        result = funcs[0](*args, **kwargs)
        for f in funcs[1:]:
            result = f(result)
        return result
    return composed


@cache
def straighten(a: tuple[int]) -> tuple[tuple[int], tuple[int]]:
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
def _compositions_list(deg, k):
    """
    Returns a list of all nonnegative integer compositions of degree `deg`
    with `k` parts, in reverse lex order.
    """
    return [
        (deg-i, *rest)
        for i in range(deg+1) 
        for rest in _compositions_list(i,k-1) 
    ] if deg > 0 and k > 1 else [(deg, *repeat(0, k-1))]
    
    
@cache
def compositions(deg, k):
    """
    Returns a `bidict` whose keys are all nonnegative integer compositions of
    `deg` degree and `k` parts and whose values are indices in *reverse lex* order
    """
    return bidict(enumerate(_compositions_list(deg, k))).inverse


@cache
def _words_list(deg, k):
    """
    Returns a list of all words of length `deg` on `k` letters, in reverse lex order
    """
    return [
        (i, *rest)
        for i in reversed(range(k))
        for rest in _words_list(deg-1, k)
    ] if deg else [()]
    

@cache
def words(deg, k):
    """
    Returns a `bidict` whose keys are all words of length `deg`
    on `k` letters and whose values are indices in *reverse lex* order
    """
    return bidict(enumerate(_words_list(deg, k))).inverse


@cache
def word_to_composition(w,k=None):
    k = max(w) + 1 if k is None else k
    c = [0] * k
    for i in w:
        c[i] += 1
    return tuple(c)


import unittest

class TestStraighten(unittest.TestCase):
    def test_0(self):
        lhs = straighten(())
        rhs = ((), ())
        self.assertEqual(lhs, rhs)

    def test_1(self):
        lhs = straighten((0,))
        rhs = ((0,), ())
        self.assertEqual(lhs, rhs)

    def test_2(self):
        lhs = straighten((0,0))
        rhs = ((0,0), ())
        self.assertEqual(lhs, rhs)

        lhs = straighten((0,1))
        rhs = ((1,0), (0,))
        self.assertEqual(lhs, rhs)

        lhs = straighten((1,0))
        rhs = ((1,0), ())
        self.assertEqual(lhs, rhs)

    def test_3(self):
        lhs = straighten((0,0,0))
        rhs = ((0,0,0), ())
        self.assertEqual(lhs, rhs)

        lhs = straighten((0,0,1))
        rhs = ((1,0,0), (0,1))
        self.assertEqual(lhs, rhs)

        lhs = straighten((0,1,0))
        rhs = ((1,0,0), (0,))
        self.assertEqual(lhs, rhs)

        lhs = straighten((1,0,0))
        rhs = ((1,0,0), ())
        self.assertEqual(lhs, rhs)

        lhs = straighten((0,1,1))
        rhs = ((1,1,0), (1,0))
        self.assertEqual(lhs, rhs)

        lhs = straighten((1,0,1))
        rhs = ((1,1,0), (1,))
        self.assertEqual(lhs, rhs)

        lhs = straighten((1,1,0))
        rhs = ((1,1,0), ())
        self.assertEqual(lhs, rhs)

        lhs = straighten((0,1,2))
        rhs = ((2,1,0), (0,1,0))
        self.assertEqual(lhs, rhs)

        lhs = straighten((1,0,2))
        rhs = ((2,1,0), (0,1))
        self.assertEqual(lhs, rhs)

        lhs = straighten((1,2,0))
        rhs = ((2,1,0), (0,))
        self.assertEqual(lhs, rhs)

        lhs = straighten((0,2,1))
        rhs = ((2,1,0), (1,0))
        self.assertEqual(lhs, rhs)
        
        lhs = straighten((2,0,1))
        rhs = ((2,1,0), (1,))
        self.assertEqual(lhs, rhs)


class TestCompositions(unittest.TestCase):
    def test_3_3(self):
        lhs = compositions(3,3)
        rhs = bidict({
            (3,0,0): 0, 
            (2,1,0): 1,
            (2,0,1): 2,
            (1,2,0): 3,
            (1,1,1): 4,
            (1,0,2): 5,
            (0,3,0): 6,
            (0,2,1): 7,
            (0,1,2): 8,
            (0,0,3): 9
        })
        self.assertEqual(lhs, rhs)


class TestWords(unittest.TestCase):
    def test_3_2(self):
        lhs = words(2,3)
        rhs = bidict({
            (2,2): 0, 
            (2,1): 1,
            (2,0): 2,
            (1,2): 3,
            (1,1): 4,
            (1,0): 5,
            (0,2): 6,
            (0,1): 7,
            (0,0): 8
        })
        self.assertEqual(lhs, rhs)


class TestWordsToCompositions(unittest.TestCase):
    def test_3_2(self):
        lhs = [(word, word_to_composition(word, 3)) for word in words(2,3)]
        rhs = [
            ((2,2), (0,0,2)), 
            ((2,1), (0,1,1)),
            ((2,0), (1,0,1)),
            ((1,2), (0,1,1)),
            ((1,1), (0,2,0)),
            ((1,0), (1,1,0)),
            ((0,2), (1,0,1)),
            ((0,1), (1,1,0)),
            ((0,0), (2,0,0))
        ]
        self.assertEqual(lhs, rhs)


if __name__ == '__main__':
    unittest.main()