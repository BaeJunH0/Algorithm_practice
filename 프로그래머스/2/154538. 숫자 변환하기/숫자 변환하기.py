from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue = deque()
    queue.append([y, 0])
    
    while queue:
        now, count = queue.popleft()
        if now == x:
            return count
        
        if now // 2 >= x and now % 2 == 0:
            queue.append([now // 2, count + 1])
        if now // 3 >= x and now % 3 == 0:
            queue.append([now // 3, count + 1])
        if now - n >= x:
            queue.append([now - n, count + 1])
            
    return -1