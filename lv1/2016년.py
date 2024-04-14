def solution(a, b):
    answer = ''
    weeks = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    days = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    now = 5
    for i in range(1, a):
        now += days[i]
    now += b - 1
    answer = weeks[now % 7]
    return answer