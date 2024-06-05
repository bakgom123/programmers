def solution(s):
    answer = 0
    same = 0
    diff = 0
    k = None
    for i in s:
        if same == diff:
            answer += 1
            k = i
        if k == i:
            same += 1
        else:
            diff += 1
    return answer