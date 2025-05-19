from sage.all import *

from functools import cache
from itertools import repeat

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
def compositions(degree, num_parts):
    """
    Returns all nonnegative integer compositions with specified degree and number of parts in lex order.
    """
    d, l = degree, num_parts
    if d == 0 or l == 1 :
        return [(d, *repeat(0, l-1))]
    else:
        return [
            (d-j, *rest)
            for j in range(d+1) 
            for rest in compositions(j,l-1) 
        ]

@cache
def words(length, num_letters):
    """
    Returns all words in num_letters letters of a given length in lex order
    """
    if length == 1 :
        return [(i,) for i in range(num_letters)]
    else:
        return [
            (i, *rest)
            for i in range(num_letters)
            for rest in words(length-1, num_letters)
        ]

@cache
def monomial_vector(f):
    """
    Returns the coefficients of a homogeneous polynomial indexed by
    compositions (exponent vectors) in lex order.
    """
    return vector(
        f[mon] 
        for mon in compositions(degree=f.degree(), num_parts=f.parent().ngens())
    )


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

if __name__ == '__main__':
    unittest.main()