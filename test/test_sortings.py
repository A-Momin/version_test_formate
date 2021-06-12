import unittest
from math import floor, sqrt
from random import randint, randrange, choice

from .utils import *
from .sortings import *
import pytest



class TestSorting(unittest.TestCase):

    def setUp(self):
        _NUM = 1000
        _sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        _repeating_sorted = [-10, -10, -10, 0, 0, 0, 0, 1, 8, 8, 9, 9, 9]
        _reverse = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        _not_sorted = [15, 8, 5, 12, 17, 18, 4, 13, 14, 19]
        _equal = [1, 1, 1, 1, 1, 1, 1, 1]
        _negative = [-1, 0, 5, -10, 20, 13, -7, 3, 2, -3]
        _negative_sorted = [-10, -7, -3, -1, 0, 2, 3, 5, 13, 20]

        self.list_of_lists = [_sorted, _repeating_sorted, _reverse,
                              _not_sorted, _equal, _negative, _negative_sorted]
        
        self.list_of_lists_B = [
            [randrange(0, _NUM) for x in range(_NUM)] for i in range(floor(sqrt(_NUM)))
        ]

    def tearDown(self):
        pass

# #************************* Insertion Sort Testings: **************************#
#     def test_insertion_sort(self):
#         for array in self.list_of_lists:
#             insertion_sort(array)
#             assert is_sorted(array)

# #************************* Selection Sort Testings: **************************#
#     def test_selection_sort(self):
#         for array in self.list_of_lists:
#             selection_sort(array)
#             assert is_sorted(array)

# #************************* Bubble Sort Testings: **************************#
    # def test_bubble_sort():
    #     my_list = [12, 5, 13, 8, 9, 65]
    #     bubble_sort(my_list)
    #     print(my_list)


#*************************** Mergesort Testings: *****************************#
    def test_merge_sort(self):

        for array in self.list_of_lists:
            L = merge_sort(array)
            assert is_sorted(L)

    def test_merge_sort_two(self):

        for array in self.list_of_lists:
            merge_sort_two(array)
            assert is_sorted(array)

    def test_merge_sort_three(self):

        for array in self.list_of_lists:
            merge_sort_three(array)
            assert is_sorted(array)

#*************************** QuickSort Testings: *****************************#

    def test_quick_sort(self):
        for array in self.list_of_lists:
            quick_sort(array)
            assert is_sorted(array)

    def test_quick_sort_two(self):

        for array in self.list_of_lists:
            quick_sort_two(array)
            assert is_sorted(array)

        for array in self.list_of_lists_B:
            quick_sort_two(array)
            assert is_sorted(array)

_NUM = 1000
_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_repeating_sorted = [-10, -10, -10, 0, 0, 0, 0, 1, 8, 8, 9, 9, 9]
_reverse = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
_not_sorted = [15, 8, 5, 12, 17, 18, 4, 13, 14, 19]
_equal = [1, 1, 1, 1, 1, 1, 1, 1]
_negative = [-1, 0, 5, -10, 20, 13, -7, 3, 2, -3]
_negative_sorted = [-10, -7, -3, -1, 0, 2, 3, 5, 13, 20]

list_of_lists = [_sorted, _repeating_sorted, _reverse, _not_sorted, _equal, _negative, _negative_sorted]
list_of_lists_B = [[randrange(0, _NUM) for x in range(_NUM)] for i in range(floor(sqrt(_NUM)))]


pytest.mark.parametrize(list_of_lists)
def test_quick_sort_two():

    for array in list_of_lists:
        quick_sort_two(array)
        assert is_sorted(array)
