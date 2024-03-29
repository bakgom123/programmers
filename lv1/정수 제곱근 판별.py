import math

def solution(n):
    num = math.sqrt(n)
    if num % 1 == 0:
        return math.pow(num+1, 2)
    else:
        return -1