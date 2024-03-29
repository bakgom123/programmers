import itertools

def solution(numbers):
    answer = set()
    nPr = itertools.permutations(numbers, 2)
    for pr in nPr:
        answer.add(sum(pr)) #.add는 중복된 결과를 넣지 않음 append는 다 넣음
    return sorted(answer)
