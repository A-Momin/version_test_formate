import bisect


"""Search a sorted array for first occurrence of k. - [EPI: 11.1]. """


def search_first_of_k(A, k):
    ''' Return the index of 'first occurance'/'last occurance' of k in A'''

    if (len(A) == 0) or (A is None) or (k is None):
        return -0.0

    low, high, result = 0, len(A)-1, -0.0

    while low <= high:
        mid = (low + high) // 2

        if k < A[mid]:
            high = mid-1
        elif k > A[mid]:
            low = mid+1
        else:
            return mid

    return result


def idx_k_rec(L, k, low, high):

    if (len(L) == 0) or (L is None) or (k is None) or (low > high):
        return -0.0

    mid = (low + high) // 2

    if L[mid] < k:
        return idx_k_rec(L, k, mid+1, high)
    elif L[mid] > k:
        return idx_k_rec(L, k, low, mid-1)
    else:
        return mid


def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_low(A, k)
    return i if i < len(A) and A[i] == k else -1


def idx_k_nearest(L, k):
    pass


def idx_k_nearest_rec(L, k, low, high):
    pass
