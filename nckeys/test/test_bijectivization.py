from unittest import TestCase

from ..word import Words, permutations
from ..bijectivization import *
from ..plactic import plactic_relations


class TestBijectivization(TestCase):

    def test_bij_neighbors(self):
        I = Bijectivization(plactic_relations(3))
        word = Word(0,1,0,1,0,2,1,0,0,1,0)
        lhs = I._neighbors(word)
        rhs = {
            Word(1,0,0,1,0,2,1,0,0,1,0),
            Word(0,1,1,0,0,2,1,0,0,1,0),
            Word(0,1,1,0,0,2,1,0,0,1,0),
            Word(0,1,0,1,2,0,1,0,0,1,0),
            Word(0,1,0,1,2,0,1,0,0,1,0),
            Word(0,1,0,1,0,2,0,1,0,1,0),
            Word(0,1,0,1,0,2,1,0,1,0,0),
        }
        self.assertEqual(lhs, rhs)

    
    def test_bij_component(self):
        """Verifying Knuth equivalence on S_4
        """
        I = Bijectivization(plactic_relations(4))

        lhs = I._component(Word(0,1,2,3))
        rhs = {Word(0,1,2,3)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(1,0,2,3))
        rhs = {Word(1,0,2,3), Word(1,2,0,3), Word(1,2,3,0)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(2,0,1,3))
        rhs = {Word(2,0,1,3), Word(0,2,1,3), Word(0,2,3,1)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(3,0,1,2))
        rhs = {Word(3,0,1,2), Word(0,3,1,2), Word(0,1,3,2)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(1,3,0,2))
        rhs = {Word(1,3,0,2), Word(1,0,3,2)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(2,3,0,1))
        rhs = {Word(2,3,0,1), Word(2,0,3,1)}
        self.assertEqual(lhs, rhs)
    
        lhs = I._component(Word(2,3,1,0))
        rhs = {Word(2,3,1,0), Word(2,1,3,0), Word(2,1,0,3)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(1,3,2,0))
        rhs = {Word(1,3,2,0), Word(3,1,2,0), Word(3,1,0,2)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(0,3,2,1))
        rhs = {Word(0,3,2,1), Word(3,0,2,1), Word(3,2,0,1)}
        self.assertEqual(lhs, rhs)

        lhs = I._component(Word(3,2,1,0))
        rhs = {Word(3,2,1,0)}
        self.assertEqual(lhs, rhs)
    

    def test_bij_nonzero_component(self):
        relations = [
            (Word(0,1), Word(1,0)),
            (Word(0,0), None)
        ]
        I = Bijectivization(relations)

        a = I._component(Word(1,1,0))
        b = I._component(Word(0,1,1,1,1,1,1,0))
        self.assertTrue(I._is_nonzero_component(a))     
        self.assertFalse(I._is_nonzero_component(b))  


    def test_bij_components(self):
        """Verifying Knuth equivalence on S_4
        """
        I = Bijectivization(plactic_relations(4))
        W = permutations(4)
        lhs = I._components(W)
        rhs = {
            Word(3,2,1,0): {Word(3,2,1,0)},
            Word(3,2,0,1): {Word(3,2,0,1), Word(3,0,2,1), Word(0,3,2,1)},
            Word(3,1,2,0): {Word(3,1,2,0), Word(1,3,2,0), Word(3,1,0,2)},
            Word(3,0,1,2): {Word(3,0,1,2), Word(0,3,1,2), Word(0,1,3,2)},
            Word(2,3,1,0): {Word(2,3,1,0), Word(2,1,3,0), Word(2,1,0,3)},
            Word(2,3,0,1): {Word(2,3,0,1), Word(2,0,3,1)},
            Word(2,0,1,3): {Word(2,0,1,3), Word(0,2,1,3), Word(0,2,3,1)},
            Word(1,2,3,0): {Word(1,2,3,0), Word(1,2,0,3), Word(1,0,2,3)},
            Word(1,3,0,2): {Word(1,3,0,2), Word(1,0,3,2)},
            Word(0,1,2,3): {Word(0,1,2,3)}
        }
        self.assertEqual(lhs, rhs)