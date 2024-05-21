def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        count += 1
        if count == 500:  # 만약 500번 이상 반복해도 1이 되지 않는다면 -1을 반환
            return -1
    return count
