import math

def solution(fees, records):
    pill = {}
    dic = {}
    for record in records:
        time, car, method = record.split()
        hour, minute = map(int, time.split(':'))
        
        if car not in dic.keys():
            pill[car] = 0
            dic[car] = [hour, minute]
        elif len(dic[car]) == 0:
            dic[car] = [hour, minute]
        else:
            pill[car] += (hour - dic[car][0]) * 60 + minute - dic[car][1] 
            dic[car] = []
    
    for i in dic.keys():
        if len(dic[i]) != 0:
            pill[i] += (23 - dic[i][0]) * 60 + 59 - dic[i][1] 
    
    answer = []
    sorted_keys = sorted(list(dic.keys()))
    for i in sorted_keys:
        time = pill[i]
        
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            addition = math.ceil((time - fees[0]) / fees[2]) * fees[3]
            answer.append(fees[1] + addition)
    
    return answer