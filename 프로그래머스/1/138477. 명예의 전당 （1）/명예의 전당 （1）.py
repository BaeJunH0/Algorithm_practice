def solution(k, score):
    answer = []
    ret = []
    for i in score:
        if len(answer) == k:
            if i > answer[-1]:
                answer[-1] = i
        else:
            answer.append(i)
        answer.sort(reverse = True)
        ret.append(min(answer))
    return ret