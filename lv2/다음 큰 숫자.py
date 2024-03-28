def solution(n):
    og = str(bin(n))
    res = n+1
    while res:
        if str(bin(res)).count('1') == og.count('1'):
            return res
        else:
            res += 1
    return res