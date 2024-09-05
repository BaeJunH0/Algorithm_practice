def solution(strArr):
    answer = 0
    dic = {}
    for i in strArr:
        if len(i) not in dic.keys():
            dic[len(i)] = 1
        else:
            dic[len(i)] += 1
    answer = max(dic.values())
    return answer