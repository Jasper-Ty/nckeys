from unittest import TestCase

from ..composition import *
from ..word import *


class TestCompositions(TestCase):
    def test_3_3(self):
        lhs = Compositions(3,3)
        rhs = [
            Composition(3,0,0), 
            Composition(2,1,0),
            Composition(2,0,1),
            Composition(1,2,0),
            Composition(1,1,1),
            Composition(1,0,2),
            Composition(0,3,0),
            Composition(0,2,1),
            Composition(0,1,2),
            Composition(0,0,3)
        ]
        self.assertEqual(lhs, rhs)


class TestCompositionsFromWords(TestCase):
    def test_3_2(self):
        lhs = [(word, Composition.from_word(word, 3)) for word in Words(2,3)]
        rhs = [
            (Word(2,2), Composition(0,0,2)), 
            (Word(2,1), Composition(0,1,1)),
            (Word(2,0), Composition(1,0,1)),
            (Word(1,2), Composition(0,1,1)),
            (Word(1,1), Composition(0,2,0)),
            (Word(1,0), Composition(1,1,0)),
            (Word(0,2), Composition(1,0,1)),
            (Word(0,1), Composition(1,1,0)),
            (Word(0,0), Composition(2,0,0))
        ]
        self.assertEqual(lhs, rhs)