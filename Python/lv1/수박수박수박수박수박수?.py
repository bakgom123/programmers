def solution(n):
    answer = ''
    if n % 2 == 0:
        answer = "수박"* (n//2)
    else:
        answer = "수박"* ((n-1)//2) + "수"
    return answer


 # return "수박" * (n//2) + "수" * (n%2)