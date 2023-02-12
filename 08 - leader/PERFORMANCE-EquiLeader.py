# A non-empty zero-indexed array A consisting of N integers is given.
#
# The leader of this array is the value that occurs in more than half of the elements of A.
#
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S]
# and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
#
# For example, given array A such that:
#
# A[0] = 4
# A[1] = 3
# A[2] = 4
# A[3] = 4
# A[4] = 4
# A[5] = 2
# we can find two equi leaders:
#
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.
#
# Write a function:
#
# def solution(A)
#     that, given a non-empty zero-indexed array A consisting of N integers, returns the number of equi leaders.
#
# For example, given:
#
# A[0] = 4
# A[1] = 3
# A[2] = 4
# A[3] = 4
# A[4] = 4
# A[5] = 2
# the function should return 2, as explained above.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
# arguments).
# Elements of input arrays can be modified.


from Test import test


def solution(A):
    equi_leaders = 0
    for i in range(0, len(A) - 1):
        first = A[0:i + 1]
        second = A[i + 1:]
        first_leader = get_leader(first)
        second_leader = get_leader(second)
        if first_leader == second_leader and (first_leader != -1 or second_leader != -1):
            equi_leaders += 1

    return equi_leaders


def get_leader(values):
    counts = {}

    for value in values:
        value_count = counts.get(value)
        if value_count is None:
            counts[value] = 1
        else:
            counts[value] = value_count + 1

    max_count = 0
    for count in counts:
        if counts[count] > max_count:
            max_count = counts[count]
            leader = count

    if max_count <= len(values) / 2:
        return -1
    else:
        return leader


test([[[4, 3, 4, 4, 4, 2]]], [2], solution)
