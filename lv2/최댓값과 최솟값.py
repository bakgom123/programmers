def solution(s):
    numS = [int(n) for n in s.split()] 
    res = str(min(numS)) + " " + str(max(numS))
    return res



# def solution(s):
#     s = list(map(int,s.split()))
#     return str(min(s)) + " " + str(max(s))
