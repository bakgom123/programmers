def solution(n):
    num = list(map(int, str(n)))
    num.sort(reverse=True)
    s = ''.join(map(str, num))
    return int(s)