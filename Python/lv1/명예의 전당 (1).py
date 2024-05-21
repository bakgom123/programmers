# def solution(k, score):
#     answer = []
#     record = []
#     for i in range(len(score)):
#         if i < k:
#             record.append(score[i])
#             answer.append(min(record))
#         else:
#             record.append(score[i])
#             record = sorted(record, reverse=True)
#             answer.append(record[k-1])
#     return answer


def solution(k, score):
    q = []
    answer = []
    for s in score:
        q.append(s)
        if len(q) > k:
            q.remove(min(q))
        answer.append(min(q))
    return answer
