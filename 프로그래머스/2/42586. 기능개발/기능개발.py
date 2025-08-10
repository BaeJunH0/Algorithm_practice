def solution(progresses, speeds):
    answer = []
    cur = 0
    
    while cur < len(progresses):
        latest = cur
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while cur < len(progresses) and progresses[cur] >= 100:
            cur += 1
        
        if cur != latest:
            answer.append(cur - latest)
            
    return answer