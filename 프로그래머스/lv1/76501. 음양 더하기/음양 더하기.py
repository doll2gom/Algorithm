def solution(absolutes, signs):
    width = len(absolutes)
    answer = 0
    for w in range(width):
        if signs[w] == True:
            answer += absolutes[w]
        else:
            answer -= absolutes[w]
    return answer