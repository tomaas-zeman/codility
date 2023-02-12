# Write a function:
#
# def solution(A, B, K)
#     that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible
#     by K, i.e.:
#
# { i : A ≤ i ≤ B, i mod K = 0 }
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible
#     by 2 within the range [6..11], namely 6, 8 and 10.
#
# Assume that:
#
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.
# Complexity:
#
# expected worst-case time complexity is O(1);
# expected worst-case space complexity is O(1).


from Test import test


def solution(A, B, K):
    if A == B:
        return 1 if A % K == 0 else 0

    lowest_divisible_number = A if A % K == 0 else A + (A % K if K < A else K - A)
    highest_divisible_number = B if B % K == 0 else B - (B % K)
    return int((highest_divisible_number - lowest_divisible_number) / K + 1)


test([[6, 11, 2], [11, 345, 17], [1, 1, 5], [0, 20000, 20000]], [3, 20, 0, 2], solution)
