# A non-empty zero-indexed array A consisting of N integers is given.
#
# A permutation is a sequence containing each element from 1 to N once, and only once.
#
# For example, array A such that:
#
# A[0] = 4
# A[1] = 1
# A[2] = 3
# A[3] = 2
# is a permutation, but array A such that:
#
# A[0] = 4
# A[1] = 1
# A[2] = 3
# is not a permutation, because value 2 is missing.
#
# The goal is to check whether array A is a permutation.
#
# Write a function:
#
# def solution(A)
#
# that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.
#
# For example, given array A such that:
#
# A[0] = 4
# A[1] = 1
# A[2] = 3
# A[3] = 2
# the function should return 1.
#
# Given array A such that:
#
# A[0] = 4
# A[1] = 1
# A[2] = 3
# the function should return 0.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
# arguments).
# Elements of input arrays can be modified.


from Test import test


def solution(A):
    # we handle cases where permutation exists and some numbers are duplicated
    # because the length must be exactly the same as the highest number
    # otherwise we get False buckets
    result = [False] * len(A)
    for i in range(len(A)):
        # fast stop - we have have a number out of bounds -> sequence is broken
        if A[i] > len(A):
            return 0
        result[A[i] - 1] = True
    return 1 if len([x for x in result if not x]) == 0 else 0


test([[[4, 1, 3, 2]], [[4, 1, 3]]], [1, 0], solution)
