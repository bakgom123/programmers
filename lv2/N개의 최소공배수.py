from functools import reduce
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(arr):
    return reduce(lcm, arr)

