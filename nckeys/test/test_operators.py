from unittest import TestCase

from ..operators import *

class TestDividedDifference(TestCase):

    def test_divided_difference_contraction(self):

        for deg in range(5):
            for n in range(5):
                for i in range(n-1):
                    lhs = divided_difference(i, deg, n) * divided_difference(i, max(deg-1,0), n)
                    rhs = Matrix(Compositions(deg, n), Compositions(max(deg-2,0), n))
                    self.assertEqual(lhs, rhs)
                

    def test_divided_difference_braid(self):
        for deg in range(5):
            for n in range(5):
                for i in range(n-2):
                    lhs = divided_difference(i, deg, n) * divided_difference(i+1, max(deg-1,0), n) * divided_difference(i, max(deg-2,0), n)
                    rhs = divided_difference(i+1, deg, n) * divided_difference(i, max(deg-1,0), n) * divided_difference(i+1, max(deg-2,0), n)
                    self.assertEqual(lhs, rhs)


class TestDemazure(TestCase):

    def test_demazure_contraction(self):
        for deg in range(5):
            for n in range(5):
                for i in range(n-1):
                    op = demazure_operator(i, deg, n)
                    lhs = op * op
                    rhs = op
                    self.assertEqual(lhs, rhs)
    

    def test_demazure_braid(self):
        for deg in range(5):
            for n in range(5):
                for i in range(n-2):
                    f = demazure_operator(i, deg, n)
                    g = demazure_operator(i+1, deg, n)
                    lhs = f * g * f
                    rhs = g * f * g
                    self.assertEqual(lhs, rhs)

    
    def test_demazure_commutation(self):
        for deg in range(5):
            for n in range(5):
                it = ((i,j) for i in range(n-1) for j in range(i+2,n-1))
                for i, j in it:
                    f = demazure_operator(i, deg, n)
                    g = demazure_operator(j, deg, n)
                    lhs = f * g
                    rhs = g * f
                    self.assertEqual(lhs, rhs)