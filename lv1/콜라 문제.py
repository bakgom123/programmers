def solution(a, b, n):
    answer = 0
    # b* (n // a) = 받은 콜라 갯수
    # 받은 콜라 갯수를 n에 다시 넣어서 돌리기
    while n >= a:
        bottles = n % a
        n = b* (n // a)
        answer += n
        n += bottles
    return answer