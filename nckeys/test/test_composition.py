from unittest import TestCase

from ..composition import *


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