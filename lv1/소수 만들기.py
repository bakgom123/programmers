from itertools import combinations


def primes(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    count = 0
    for i in combinations(nums, 3):
        if primes(sum(i)):
            count += 1

    return count
