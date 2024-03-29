def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:
            continue
        elif signs[i] == False:
            absolutes[i] *= -1
    return sum(absolutes)