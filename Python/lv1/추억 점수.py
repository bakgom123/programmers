def solution(name, yearning, photo):
    answer = []
    for pic in photo:
        score = 0
        for i in range(len(name)):
            score += pic.count(name[i]) * yearning[i]
        answer.append(score)

    return answer
