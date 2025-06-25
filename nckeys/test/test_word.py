from unittest import TestCase

from ..word import *


class TestRewrites(TestCase):
    def test_rewrites(self):
        lword = Word(1,2,1)
        rword = Word(2,1,1)
        word = Word(1,2,1,2,1,3,3,2,1,2,1)
        lhs = list(word.rewrites(lword, rword))
        rhs = [
            Word(2,1,1,2,1,3,3,2,1,2,1),
            Word(1,2,2,1,1,3,3,2,1,2,1),
            Word(1,2,2,1,1,3,3,2,2,1,1),
        ]
        pass


class TestSlice(TestCase):

    def test_slice(self):
        lhs = Word(0,1,2,3,4)[0:3]
        rhs = Word(0,1,2)
        self.assertEqual(lhs, rhs)


class TestWords(TestCase):

    def test_words_2_3(self):
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


    def test_words_3_0(self):
        lhs = Words(3,0)
        rhs = []
        self.assertEqual(lhs, rhs)

    
    def test_words_3_1(self):
        lhs = Words(3,1)
        rhs = [Word(0,0,0)]
        self.assertEqual(lhs, rhs)
    
    
    def test_words_3_2(self):
        lhs = Words(3,2)
        rhs = [
            Word(1,1,1),
            Word(1,1,0),
            Word(1,0,1),
            Word(1,0,0),
            Word(0,1,1),
            Word(0,1,0),
            Word(0,0,1),
            Word(0,0,0)
        ]
        self.assertEqual(lhs, rhs)


    def test_words_3_3(self):
        lhs = Words(3,3)
        rhs = [
            Word(1,1,1),
            Word(1,1,0),
            Word(1,0,1),
            Word(1,0,0),
            Word(0,1,1),
            Word(0,1,0),
            Word(0,0,1),
            Word(0,0,0)
        ]
        pass
