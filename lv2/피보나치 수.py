def solution(n):
    fibo = [0, 1]
    res = 0
    for i in range(2, n+1):
        answer = fibo[i - 2] + fibo[i - 1]
        fibo.append(answer)
    return fibo[-1] % 1234567