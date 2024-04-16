import unittest
from main import arrayAlgs

class TestArrayAlgs(unittest.TestCase):
    def setUp(self):
        self.arr = arrayAlgs()

    def test_badThirteen_emptyArray(self):
        result = self.arr.badThirteen([])
        self.assertEqual(result, [])

    def test_badThirteen_noThirteen(self):
        result = self.arr.badThirteen([1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_badThirteen_singleThirteen(self):
        result = self.arr.badThirteen([13])
        self.assertEqual(result, [])

    def test_badThirteen_multipleThirteens(self):
        result = self.arr.badThirteen([4, 2, 13, 13])
        self.assertEqual(result, [4, 2])

    def test_badThirteen_allThirteen(self):
        result = self.arr.badThirteen([13, 13, 13])
        self.assertEqual(result, [])

    def test_badThirteen_noModification(self):
        result = self.arr.badThirteen([1, 2, 3, 4])
        self.assertEqual(result, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
