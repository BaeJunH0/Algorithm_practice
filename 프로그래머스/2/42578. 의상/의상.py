import math

def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] not in dic.keys():
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    comb = 1
    for i in dic.keys():
        comb *= dic[i] + 1
    return comb-1
    