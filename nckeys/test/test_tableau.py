from unittest import TestCase

from ..tableau import *

class TestRows(TestCase):
    
    def test_rows(self):
        lhs = get_rows([5,4,3,5,3,10,2,1,1,1,4,3])
        rhs = [[5,4,3], [5,3], [10,2,1,1,1], [4,3]]
        self.assertEqual(lhs, rhs)


class TestTableauWord(TestCase):
    
    def test_tableau(self):
        lhs = tableau([2,6,1,5,4,3])
        rhs = [[1,3],[2,4],[5],[6]]
        self.assertEqual(lhs, rhs)


    def test_tableau_word(self):
        lhs = tableau_word([2,6,1,5,4,3])
        rhs = (6,5,2,4,1,3)
        self.assertEqual(lhs, rhs)

