# def solution(a, b):
#     res = 0
#     q = min(a,b)
#     w = max(a,b)
#     if a == b:
#         return a
#     for i in range(q, w+1):
#         res += q
#         q += 1
#     return res

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))