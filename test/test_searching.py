from searching import *
import unittest
import pytest
from random import *

data = [[[*range(5)], 2, 2], [[5, 4, 3, 2], 5, 0],
        [[0], 1, -0.0], [[1, 3, 6, 9], 9, 3]]


@pytest.mark.parametrize("L, k, expected", data)
def test_search_first_of_k(L, k, expected):
    assert search_first_of_k(L, k) == expected


class TestBinarySearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.L0 = [[[*range(5)], 2, 2], [[5, 4, 3, 2], 5, 0],
                  [[0], 1, -0.0], [[1, 3, 6, 9], 9, 3]]

    def setUp(self):
        r = randrange(0, 1000)
        self.L1 = [[[*range(5)], 2, 2], [[5, 4, 3, 2], 5, 0],
                   [[0], 1, -0.0], [[1, 3, 6, 9], 9, 3]]
        self.k = choice([*range(-10, 10)])

    # @pytest.mark.parametrize("L, k, expected", self.L1)
    def test_search_first_of_k(self, L, k, expected):
        assert search_first_of_k(L, k) == expected

    # def test_idx_k_rec(self):
    #     self.assertEqual(self.k, self.L[idx_k_rec(
    #         self.L, self.k, 0, len(self.L)-1)])

    # def test_idx_k_nearnest(self):
    #     self.assertEqual(self.k, self.L[idx_k_nearest(self.L, self.k)])

    # def test_idx_k_nearest_rec(self):
    #     self.assertEqual(self.k, self.L[idx_k_nearest_rec(
    #         self.L, self.k, 0, len(self.L)-1)])

    def tearDown(self):
        pass


####################################################################
####################################################################
