from random import randint, randrange
from typing import List
import sys
from utils import *



"""Implement Selection sort. """


"""Implementation of Insertion Sort."""


"""Implementation of Bubble Sort."""

# NOT TESTED !!
def bubble_sort(L):
    for j in range(len(L)): 
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp


#--------------------------------------------------
"""Implementation of merge sort algorithm.

This modules provides several methods, implemented in various way, for
sorting a list using mergesort algorithm.
"""


def merge_sort(L: List) -> List:
    """Sorts and returns the specified list using merge-sort algorithm.

    Args:
        L: the list to be sorted
    Returns:
        a sorted list containing all elements of the given list, L
    """

    N = len(L)
    if N <= 1:
        return L

    mid = N // 2
    left = merge_sort(L[0: mid])
    right = merge_sort(L[mid:])
    return merge(left, right)


def merge(L1: List, L2: List) -> List:
    """It returns a sorted list after stably merging L1 with L2.

    Args:
        L1: sorted list to be merged with L2 into a new list
        L2: sorted list to be merged with L1 into a new list
    Returns:
        a sorted list containing all elements of both list - L1 and L2.
    """
    L = L1 + L2
    left_index, right_index = 0, 0

    for i in range(len(L)):
        if left_index >= len(L1):
            L[i] = L2[right_index]
            right_index += 1
        elif right_index >= len(L2):
            L[i] = L1[left_index]
            left_index += 1
        elif L2[right_index] < L1[left_index]:   # ensure stability
            L[i] = L2[right_index]
            right_index += 1
        else:
            L[i] = L1[left_index]
            left_index += 1
    return L


#************************ Alternative implementations ************************#
def merge_sort_two(a: List) -> None:
    """Sorts the  specified list using merge-sort algorithm.

    Args:
        a: the list to be sorted
    """
    _merge_sort_two(a, 0, len(a)-1)


def _merge_sort_two(a: List, low: int, high: int) -> None:
    """It sorts a[low ... high] by first deviding it into a[low ... mid] and
    a[mid+1 ... high] and then merging them

    Args:
        a   : the array to be sorted
        low : first index of first half of the array, a[low ... mid]
        high: last index of second half of the array, a[mid+1 ... high]
    """
    if low >= high:
        return

    mid = (low + high) // 2

    # sorts first half of the array, a[low ... mid]
    _merge_sort_two(a, low, mid)

    # sorts first half of the array, a[mid+1 ... high]
    _merge_sort_two(a, mid + 1, high)

    # merges a[low ... mid] and a[mid+1 ... high], two halves of the array
    merge_two(a, low, mid, high)


def merge_two(a: List, low: int, mid: int, high: int):
    """It stably merges a[low ... mid] with a[mid+1 ... high] using an
    auxilary array, aux[low ... high]

    Args:
        a   : the array is being sorted
        low : initial index of first half of the array, a[low ... mid]
        mid : last index of first half of the array, a[low ... mid]
        high: last index of second half of the array, a[mid+1 ... high]
    """

    aux = [item for item in a]
    left, right, i = low, mid+1, low

    while left <= mid and right <= high:
        if aux[left] <= aux[right]:       # ensures stability
            a[i] = aux[left]
            left += 1
            i += 1
        else:
            a[i] = aux[right]
            right += 1
            i += 1

    while left <= mid:
        a[i] = aux[left]
        i += 1
        left += 1


#************************ Alternative implementations ************************#

def merge_sort_three(a: List):
    """Sorts the  specified list using merge-sort algorithm.

    Args:
        a: the list to be sorted
    """
    aux = [None]*len(a)
    _merge_sort_three(a, 0, len(a)-1, aux)


def _merge_sort_three(a: List, low: int, high: int, aux: List) -> None:
    """It sorts a[low ... high] by first deviding it into a[low ... mid] and
    a[mid+1 ... high] and then merging them

    Args:
        a   : the array to be sorted
        low : first index of first half of the array, a[low ... mid]
        high: last index of second half of the array, a[mid+1 ... high]
        aux : the auxilary array for recycling
    """
    if low >= high:
        return
    mid = (low + high) // 2

    # sorts first half of the array, a[low ... mid]
    _merge_sort_three(a, low, mid, aux)

    # sorts first half of the array, a[mid+1 ... high]
    _merge_sort_three(a, mid + 1, high, aux)

    # merges a[low ... mid] and a[mid+1 ... high], two halves of a[low...high]
    merge_three(a, low, mid, high, aux)


def merge_three(a: List, low: int, mid: int, high: int, aux: List) -> None:
    """It stably merges a[low ... mid] with a[mid+1 ... high] using an
    auxilary array, aux[low ... high]

    Args:
        a   : the array is being sorted
        low : first index of first half of the array, a[low ... mid]
        mid : last index of first half of the array, a[low ... mid]
        high: last index of second half of the array, a[mid+1 ... high]
        aux : the auxilary array for recycling
    """
    for i in range(low, high+1):
        aux[i] = a[i]

    left_index, right_index = low, mid+1

    for i in range(low, high+1):
        if left_index > mid:
            a[i] = aux[right_index]
            left_index += 1
        elif right_index > high:
            a[i] = aux[left_index]
            right_index += 1
        elif aux[right_index] < aux[left_index]:   # ensures stability
            a[i] = aux[right_index]
            right_index += 1
        else:
            a[i] = aux[left_index]
            left_index += 1


""" Implementation of quick sort algorithm.

This modules provides two functions, implemented in different ways, for
sorting a list using quicksort algorithm.
"""


def quick_sort(a):

    def _quick_sort(a, low, high):
        if low >= high:
            return
        pi = partition(a, low, high)  # pi -> Pivot Index
        _quick_sort(a, low, pi-1)
        _quick_sort(a, pi+1, high)

    def partition(a, low, high):

        pivot, pi = a[high], low      # pi -> Pivot Index

        for i in range(low, high):
            if a[i] < pivot:
                swap(a, pi, i)
                pi = pi+1

        swap(a, pi, high)
        return pi

    # called the quicksort procedure
    _quick_sort(a, 0, len(a)-1)


def quick_sort_two(a):

    def _quick_sort_two(a, low, high):
        if low >= high:
            return
        pi = partition_two(a, low, high)  # pi -> Pivot Index
        _quick_sort_two(a, low, pi-1)
        _quick_sort_two(a, pi+1, high)

    def partition_two(a, low, high):
        """ partition the subarray a[low, ..., high].

        it partition the subarray a[low, ..., high] so that a[lo..j-1] <= a[j] <=
        a[j+1..hi] and return the index j.

        Args:
            a     -> the array to be partioned
            low   -> the lower index into the specified array
            hight -> the upper index into the specified array

        """
        pivot, i, j = a[low], low + 1, high
        while True:
            while a[i] < pivot:    # find item on low to swap
                if i == high:
                    break
                i += 1

            while a[j] >= pivot:    # find item on high to swap
                if j == low:
                    break  # redundant since a[low] acts as sentinel
                j -= 1

            if i >= j:
                break        # check if pointers cross

            swap(a, i, j)

        swap(a, low, j)             # put partitioning item pivot at a[j]

        # now, a[low ... j-1] <= a[j] <= a[j+1 ... high]
        return j

    # called the quicksort procedure
    _quick_sort_two(a, 0, len(a)-1)

"""Implementations of Least Significant Digit Radix Sort."""



"""Implementations of Most Significant Digit Radix Sort."""

# LSD -> Least Significent Digit
def LSD_radix_sort(a: list, word_len: int):
    """
    Args:
        a: list of stirng of SAME length.
        w: length of a item (string) in the list, a.
    """
    aux = [None]*len(a)
    RADIX = 256

    for w in reversed(range(word_len)):
        count = [0]*(RADIX+1)
        for i in range(len(a)):
            count[ord(a[i][w])+1] += 1
        for i in range(RADIX):
            count[i+1] += count[i]
        for i in range(len(a)):
            aux[count[ord(a[i][w])]] = a[i]
            count[ord(a[i][w])] += 1
        for i in range(len(a)):
            a[i] = aux[i]
