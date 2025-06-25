from unittest import TestCase

from ..lib import *


class TestSubsequences(TestCase):

    def test_subsequences_0_0(self):
        lhs = list(subsequences_of_n(0,0))
        rhs = [()]
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_0_1(self):
        lhs = list(subsequences_of_n(0,1))
        rhs = []
        self.assertEqual(lhs, rhs)

    
    def test_subsequences_0_2(self):
        lhs = list(subsequences_of_n(0,2))
        rhs = []
        self.assertEqual(lhs, rhs)

    
    def test_subsequences_0_3(self):
        lhs = list(subsequences_of_n(0,3))
        rhs = []
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_1_0(self):
        lhs = list(subsequences_of_n(1,0))
        rhs = [()]
        self.assertEqual(lhs, rhs)

    
    def test_subsequences_1_1(self):
        lhs = list(subsequences_of_n(1,1))
        rhs = [(0,)]
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_1_2(self):
        lhs = list(subsequences_of_n(1,2))
        rhs = []
        self.assertEqual(lhs, rhs)


    def test_subsequences_1_3(self):
        lhs = list(subsequences_of_n(1,3))
        rhs = []
        self.assertEqual(lhs, rhs)

    
    def test_subsequences_2_0(self):
        lhs = list(subsequences_of_n(2,0))
        rhs = [()]
        self.assertEqual(lhs, rhs)

    
    def test_subsequences_2_1(self):
        lhs = list(subsequences_of_n(2,1))
        rhs = [(0,), (1,)]
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_2_2(self):
        lhs = list(subsequences_of_n(2,2))
        rhs = [(0,1)]
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_2_3(self):
        lhs = list(subsequences_of_n(2,3))
        rhs = []
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_3_0(self):
        lhs = list(subsequences_of_n(3,0))
        rhs = [()]
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_3_1(self):
        lhs = list(subsequences_of_n(3,1))
        rhs = [(0,), (1,), (2,)]
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_3_2(self):
        lhs = list(subsequences_of_n(3,2))
        rhs = [(0,1),(0,2),(1,2)]
        self.assertEqual(lhs, rhs)
    

    def test_subsequences_3_3(self):
        lhs = list(subsequences_of_n(3,3))
        rhs = [(0,1,2)]
        self.assertEqual(lhs, rhs)


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


class TestWindows(TestCase):

    def test_windows_0(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 0))
        rhs = [
            ([], [], [0,1,2,3,4,5,6,7,8,9,10]),
            ([0], [], [1,2,3,4,5,6,7,8,9,10]),
            ([0,1], [], [2,3,4,5,6,7,8,9,10]),
            ([0,1,2], [], [3,4,5,6,7,8,9,10]),
            ([0,1,2,3], [], [4,5,6,7,8,9,10]),
            ([0,1,2,3,4], [], [5,6,7,8,9,10]),
            ([0,1,2,3,4,5], [], [6,7,8,9,10]),
            ([0,1,2,3,4,5,6], [], [7,8,9,10]),
            ([0,1,2,3,4,5,6,7], [], [8,9,10]),
            ([0,1,2,3,4,5,6,7,8], [], [9,10]),
            ([0,1,2,3,4,5,6,7,8,9], [], [10]),
            ([0,1,2,3,4,5,6,7,8,9,10], [], []),
        ]
        self.assertEqual(lhs, rhs)

    
    def test_windows_1(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 1))
        rhs = [
            ([], [0], [1,2,3,4,5,6,7,8,9,10]),
            ([0], [1], [2,3,4,5,6,7,8,9,10]),
            ([0,1], [2], [3,4,5,6,7,8,9,10]),
            ([0,1,2], [3], [4,5,6,7,8,9,10]),
            ([0,1,2,3], [4], [5,6,7,8,9,10]),
            ([0,1,2,3,4], [5], [6,7,8,9,10]),
            ([0,1,2,3,4,5], [6], [7,8,9,10]),
            ([0,1,2,3,4,5,6], [7], [8,9,10]),
            ([0,1,2,3,4,5,6,7], [8], [9,10]),
            ([0,1,2,3,4,5,6,7,8], [9], [10]),
            ([0,1,2,3,4,5,6,7,8,9], [10], []),
        ]
        self.assertEqual(lhs, rhs)
    
    
    def test_windows_2(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 2))
        rhs = [
            ([], [0,1], [2,3,4,5,6,7,8,9,10]),
            ([0], [1,2], [3,4,5,6,7,8,9,10]),
            ([0,1], [2,3], [4,5,6,7,8,9,10]),
            ([0,1,2], [3,4], [5,6,7,8,9,10]),
            ([0,1,2,3], [4,5], [6,7,8,9,10]),
            ([0,1,2,3,4], [5,6], [7,8,9,10]),
            ([0,1,2,3,4,5], [6,7], [8,9,10]),
            ([0,1,2,3,4,5,6], [7,8], [9,10]),
            ([0,1,2,3,4,5,6,7], [8,9], [10]),
            ([0,1,2,3,4,5,6,7,8], [9,10], []),
        ]
        self.assertEqual(lhs, rhs)

    
    def test_windows_3(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 3))
        rhs = [
            ([], [0,1,2], [3,4,5,6,7,8,9,10]),
            ([0], [1,2,3], [4,5,6,7,8,9,10]),
            ([0,1], [2,3,4], [5,6,7,8,9,10]),
            ([0,1,2], [3,4,5], [6,7,8,9,10]),
            ([0,1,2,3], [4,5,6], [7,8,9,10]),
            ([0,1,2,3,4], [5,6,7], [8,9,10]),
            ([0,1,2,3,4,5], [6,7,8], [9,10]),
            ([0,1,2,3,4,5,6], [7,8,9], [10]),
            ([0,1,2,3,4,5,6,7], [8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)

    
    def test_windows_4(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 4))
        rhs = [
            ([], [0,1,2,3], [4,5,6,7,8,9,10]),
            ([0], [1,2,3,4], [5,6,7,8,9,10]),
            ([0,1], [2,3,4,5], [6,7,8,9,10]),
            ([0,1,2], [3,4,5,6], [7,8,9,10]),
            ([0,1,2,3], [4,5,6,7], [8,9,10]),
            ([0,1,2,3,4], [5,6,7,8], [9,10]),
            ([0,1,2,3,4,5], [6,7,8,9], [10]),
            ([0,1,2,3,4,5,6], [7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)
    
    
    def test_windows_5(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 5))
        rhs = [
            ([], [0,1,2,3,4], [5,6,7,8,9,10]),
            ([0], [1,2,3,4,5], [6,7,8,9,10]),
            ([0,1], [2,3,4,5,6], [7,8,9,10]),
            ([0,1,2], [3,4,5,6,7], [8,9,10]),
            ([0,1,2,3], [4,5,6,7,8], [9,10]),
            ([0,1,2,3,4], [5,6,7,8,9], [10]),
            ([0,1,2,3,4,5], [6,7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)
        
    
    def test_windows_6(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 6))
        rhs = [
            ([], [0,1,2,3,4,5], [6,7,8,9,10]),
            ([0], [1,2,3,4,5,6], [7,8,9,10]),
            ([0,1], [2,3,4,5,6,7], [8,9,10]),
            ([0,1,2], [3,4,5,6,7,8], [9,10]),
            ([0,1,2,3], [4,5,6,7,8,9], [10]),
            ([0,1,2,3,4], [5,6,7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)
    

    def test_windows_7(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 7))
        rhs = [
            ([], [0,1,2,3,4,5,6], [7,8,9,10]),
            ([0], [1,2,3,4,5,6,7], [8,9,10]),
            ([0,1], [2,3,4,5,6,7,8], [9,10]),
            ([0,1,2], [3,4,5,6,7,8,9], [10]),
            ([0,1,2,3], [4,5,6,7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)


    def test_windows_8(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 8))
        rhs = [
            ([], [0,1,2,3,4,5,6,7], [8,9,10]),
            ([0], [1,2,3,4,5,6,7,8], [9,10]),
            ([0,1], [2,3,4,5,6,7,8,9], [10]),
            ([0,1,2], [3,4,5,6,7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)


    def test_windows_9(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 9))
        rhs = [
            ([], [0,1,2,3,4,5,6,7,8], [9,10]),
            ([0], [1,2,3,4,5,6,7,8,9], [10]),
            ([0,1], [2,3,4,5,6,7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)
    

    def test_windows_10(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 10))
        rhs = [
            ([], [0,1,2,3,4,5,6,7,8,9], [10]),
            ([0], [1,2,3,4,5,6,7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)
    

    def test_windows_11(self):
        lhs = list(windows([0,1,2,3,4,5,6,7,8,9,10], 11))
        rhs = [
            ([], [0,1,2,3,4,5,6,7,8,9,10], []),
        ]
        self.assertEqual(lhs, rhs)