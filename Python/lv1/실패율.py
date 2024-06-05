from collections import Counter

def solution(N, stages):
    answer = []
    fail_dict = {}
    stages.sort()
    count = Counter(stages)
    total_players = len(stages)

    for stage in range(1, N+1):
        if total_players != 0:
            failed_players = count[stage]
            fail_rate = failed_players / total_players
            fail_dict[stage] = fail_rate
            total_players -= failed_players
        else:
            fail_dict[stage] = 0

    answer = sorted(fail_dict, key=lambda x: fail_dict[x], reverse=True)
    
    return answer