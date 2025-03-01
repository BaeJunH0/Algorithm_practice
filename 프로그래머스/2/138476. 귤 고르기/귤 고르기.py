def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        if t in dic.keys():
            dic[t] += 1
        else:
            dic[t] = 1
            
    arr = sorted(list(dic.values()), reverse = True)
    for element in arr:
        k -= element
        answer += 1
        if k <= 0:
            break
        
    return answer