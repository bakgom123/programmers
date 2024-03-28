def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    res = []

    for i in range(len(A)):
        res.append(A[i] * B[i])

    return sum(res)

