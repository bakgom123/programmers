def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


# 내가 작성한 코드인데 효율성 테스트랑 테스트 케이스 10, 11, 12 는 통과를 못 했다

# def primes(a):
#     for i in range(2, a):
#         if a % i == 0:
#             return False
#     return True

# def solution(n):
#     answer = 0
#     for i in range(2, n+1):
#         if primes(i):
#             answer += 1
#     return answer


# # 에라토스테네스의 체
# def solution(n):
#     # n까지의 숫자들이 소수인지 여부를 저장하는 리스트를 생성합니다.
#     # 초기에는 모든 수가 소수라고 가정하고 True로 초기화합니다.
#     sieve = [True] * (n+1)

#     # 0과 1은 소수가 아니므로 False로 설정합니다.
#     sieve[0] = sieve[1] = False

#     # 에라토스테네스의 체 알고리즘을 사용하여 소수를 찾습니다.
#     # 2부터 n의 제곱근까지의 범위에서 반복합니다.
#     for i in range(2, int(n**0.5)+1):
#         # 현재 숫자가 소수인 경우
#         if sieve[i]:
#             # 현재 숫자의 배수들을 소수가 아니라고 표시합니다.
#             # i의 제곱부터 n까지 i씩 증가하면서 배수를 확인합니다.
#             for j in range(i*i, n+1, i):
#                 sieve[j] = False

#     # 소수를 찾은 결과를 토대로 True의 개수를 세어 반환합니다.
#     return sum(sieve)
