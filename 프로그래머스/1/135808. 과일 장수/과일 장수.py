def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    temp = []
    for i in range(len(score)):
        temp.append(score[i])
        if (i + 1) % m == 0:
            answer += min(temp) * m
            temp = []
    return answer