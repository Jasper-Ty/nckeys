from unittest import TestCase

from ..word import *


class TestM(TestCase):
    def test_0(self):
        w = Word(1,2,3,4)
    
    def test_1(self):
        w = Word(1,2,3,4)


class TestWords(TestCase):
    """
    Tests the Words() function against hand-computed lists
    """

    def test_words_3_2(self):
        lhs = Words(2,3)
        rhs = [
            Word(2,2), 
            Word(2,1),
            Word(2,0),
            Word(1,2),
            Word(1,1),
            Word(1,0),
            Word(0,2),
            Word(0,1),
            Word(0,0)
        ]
        self.assertEqual(lhs, rhs)


    def test_words_3_3(self):
        lhs = Words(2,3)
        rhs = [
            Word(2,2), 
            Word(2,1),
            Word(2,0),
            Word(1,2),
            Word(1,1),
            Word(1,0),
            Word(0,2),
            Word(0,1),
            Word(0,0)
        ]
        self.assertEqual(lhs, rhs)