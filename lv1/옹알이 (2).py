def solution(babbling):
    answer = 0

    for word in babbling:
        for sound in ["aya", "ye", "woo", "ma"]:
            if sound * 2 not in word:
                word = word.replace(sound, "1")
        if word.isdigit():
            answer += 1

    return answer
