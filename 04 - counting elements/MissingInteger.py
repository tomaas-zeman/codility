# Write a function:
#
# def solution(A)
#
# that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0)
# that does not occur in A.
#
# For example, given:
#
#   A[0] = 1
#   A[1] = 3
#   A[2] = 6
#   A[3] = 4
#   A[4] = 1
#   A[5] = 2
# the function should return 5.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
# arguments).
# Elements of input arrays can be modified.


from Test import test


def solution(A):
    sorted_list = [x for x in sorted(A) if x > 0]
    previous_value = 0
    for n in sorted_list:
        if n - previous_value == 1:
            previous_value = n
    return previous_value + 1


test([
    [[1, 3, 6, 4, 1, 2]],
    [[2]],
    [[-2]],
    [[1]],
    [[-10, -5, 0, 1, 2, 3, 5]],
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [[0, 1, 2, 3, 4, 5, 6, 8, 9, 10]]
], [5, 1, 1, 2, 4, 11, 7], solution)
