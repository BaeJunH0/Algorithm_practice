from collections import deque

def solution(maps):   
    queue = deque()
    queue.append((0, 0, 1))
    
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    while queue:
        x, y, count = queue.popleft()
        
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return count
        
        for a, b in directions:
            nx, ny = x + a, y + b
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count + 1))
            
    return -1