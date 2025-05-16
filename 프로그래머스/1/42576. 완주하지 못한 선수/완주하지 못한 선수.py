def solution(participant, completion):
    dic = {}
    
    for i in completion:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    
    for i in participant:
        # 종료 조건 1. 완주자 명단에 없는 경우
        if i not in dic.keys():
            return i
        
        # 종료 조건 2. 동명이인이 완주자 명단에 있는 경우
        dic[i] -= 1
        if dic[i] < 0:
            return i