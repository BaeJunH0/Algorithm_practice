from collections import deque

def solution(n, computers):
    target = []
    
    adj_list = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(0, i + 1):
            if i != j and computers[i][j] == 1:
                adj_list[i].append(j)
                adj_list[j].append(i)
    
    visited = [0] * n
    count = 0
    for i in range(n):
        if visited[i] == 1:
            continue
        
        queue = deque()
        queue.append(i)
        
        while queue:
            target = queue.popleft()
            
            for t in adj_list[target]:
                if visited[t] == 0:
                    visited[t] = 1
                    queue.append(t)
        count += 1
    
    return count
            