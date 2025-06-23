from unittest import TestCase

from ..lib import *

class Test2String(TestCase):
    def test_0(self):
        comp = (3,5,0,2,1)
        lhs = sl2string(comp, 1, 3)
        rhs = [
            (3,5,0,2,1), 
            (3,4,0,3,1),
            (3,3,0,4,1),
            (3,2,0,5,1)
        ]
        self.assertEqual(lhs, rhs)


    def test_1(self):
        comp = (3,2,0,5,1)
        lhs = sl2string(comp, 1, 3)
        rhs = [
            (3,2,0,5,1), 
            (3,3,0,4,1),
            (3,4,0,3,1),
            (3,5,0,2,1)
        ]
        self.assertEqual(lhs, rhs)

    
    def test_2(self):
        comp = (3,4,0,4,1)
        lhs = sl2string(comp, 1, 3)
        rhs = [
            (3,4,0,4,1), 
        ]
        self.assertEqual(lhs, rhs)


class TestStraighten(TestCase):
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


class TestWordsToCompositions(TestCase):
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