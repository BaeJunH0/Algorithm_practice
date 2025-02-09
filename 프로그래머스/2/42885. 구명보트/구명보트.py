from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    d = deque(people)
    
    while len(d) > 0:
        temp = 0
        temp += d.pop()
        if len(d) > 0 and temp + d[0] <= limit:
            temp += d.popleft()
        answer += 1
        
    return answer