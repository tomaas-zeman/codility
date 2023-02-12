# We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of N non-negative integers,
# specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
#
# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point
# (assuming that the discs contain their borders).
#
# The figure below shows discs drawn for N = 6 and A as follows:
#
#     A[0] = 1
#     A[1] = 5
#     A[2] = 2
#     A[3] = 1
#     A[4] = 4
#     A[5] = 0
#
#
# There are eleven (unordered) pairs of discs that intersect, namely:
#
# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:
#
# def solution(A)
#     that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of
#     intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
#
# Given array A shown above, the function should return 11, as explained above.
#
# Assume that:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].
# Complexity:
#
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
# arguments).
# Elements of input arrays can be modified.


from Test import test
from functools import cmp_to_key


class Bound:
    def __init__(self, uid, value, add, is_left):
        self.uid = uid
        self.value = value
        self.add = add
        self.is_left = is_left


def sort_bounds(b1, b2):
    result = b1.value - b2.value

    if result == 0:
        if b1.is_left:
            return -1
        elif b2.is_left:
            return 1

    return result


def solution(A):
    bounds = []

    for i in range(0, len(A)):
        bounds.append(Bound(i, i - A[i], i + A[i], True))
        bounds.append(Bound(i, i + A[i], i - A[i], False))

    bounds = sorted(bounds, key=cmp_to_key(sort_bounds))

    intersections = 0
    open_intersections = 0
    for b in bounds:
        if b.is_left:
            intersections += open_intersections
            open_intersections += 1
        else:
            open_intersections -= 1

    if intersections > 10000000:
        return -1

    return intersections


test([[[1, 5, 2, 1, 4, 0]]], [11], solution)
