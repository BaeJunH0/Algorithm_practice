from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [1] * n
    
    for i in range(n):
        if visited[i] == 0:
            continue
        else:
            queue.append(i)
        while len(queue) != 0:
            target = queue.popleft()
            visited[target] = 0

            for j in range(n):
                if visited[j] == 1 and computers[target][j] == 1:
                    queue.append(j)
        answer += 1
    return answer