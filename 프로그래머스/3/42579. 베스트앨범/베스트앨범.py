def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(plays)):
        if genres[i] not in dic.keys():
            dic[genres[i]] =  plays[i]
        else:
            dic[genres[i]] += plays[i]
    
    gs = []
    values = list(dic.values())
    values.sort(reverse = True)
    
    for i in values:
        for j in dic.keys():
            if i == dic[j]:
                gs.append(j)
    
    for i in gs:
        arr = []
        for j in range(len(plays)):
            if i == genres[j]:
                arr.append(j)
        arr.sort(reverse = True, key=lambda x:plays[x])
        arr = arr[:2]
        answer += arr
    
    return answer