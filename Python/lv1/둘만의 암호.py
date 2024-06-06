def solution(s, skip, index):
    letters = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for i in list(skip):
        letters = letters.replace(i,"")
        
    for a in s:
        answer += letters[(letters.find(a) + index) % len(letters)]
    return answer