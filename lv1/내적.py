def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer



# solution = lambda x, y: sum(a*b for a, b in zip(x, y))