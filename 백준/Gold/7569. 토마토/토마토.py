import sys
from collections import deque

input = sys.stdin.readline

x, y, z = map(int, input().rstrip().split())

tomato = []

queue = deque()

for i in range(z):
    temp = []
    for j in range(y):
        line = list(map(int, input().rstrip().split()))
        
        for k in range(len(line)):
            if line[k] == 1:
                queue.append((i, j, k))

        temp.append(line)

    tomato.append(temp)

visited = [[[True] * x for _ in range(y)] for __ in range(z)]
for a, b, c in queue:
    visited[a][b][c] = False

dir = [(0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1)]

count = 0

while True:
    next = deque()
    
    while queue:
        _z, _y, _x = queue.popleft()

        for a, b, c in dir:
            nx, ny, nz = _x + a, _y + b, _z + c

            if 0 <= nx < x and 0 <= ny < y and 0 <= nz < z and visited[nz][ny][nx] and tomato[nz][ny][nx] != -1:
                tomato[nz][ny][nx] = 1
                visited[nz][ny][nx] = False
                next.append((nz, ny, nx))
    
    if not next:
        break

    count += 1
    queue = next

for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()

print(count)