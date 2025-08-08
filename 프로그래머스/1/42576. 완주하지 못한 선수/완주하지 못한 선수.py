def solution(participant, completion):
    dic = {}
    for i in completion:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    
    for i in participant:
        if i not in dic.keys() or dic[i] == 0:
            return i
        else:
            dic[i] -= 1