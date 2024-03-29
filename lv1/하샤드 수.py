def solution(x):
    res = sum([int(n) for n in str(x)])

    if x % res == 0:
        return True
    else:
        return False
             