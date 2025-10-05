import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().rstrip().split())

maze = []

for _ in range(row):
    line = input().rstrip()
    temp = []

    for ele in line:
        temp.append(int(ele))

    maze.append(temp)

queue = deque()
queue.append((0, 0, 1, 0))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

check = [[[True] * 2 for _ in range(col)] for __ in range(row)]

min_count = 10 ** 6
while queue:
    x, y, count, is_broken = queue.popleft()

    if x == row - 1 and y == col - 1:
        min_count = min(min_count, count)
    
    for a, b in dirs:
        nx, ny = x + a, y + b

        if 0 <= nx < row and 0 <= ny < col:
            if maze[nx][ny] == 0 and check[nx][ny][is_broken]:
                queue.append((nx, ny, count + 1, is_broken))
                check[nx][ny][is_broken] = False
            if maze[nx][ny] == 1 and is_broken == 0 and check[nx][ny][is_broken + 1]:
                queue.append((nx, ny, count + 1, is_broken + 1))
                check[nx][ny][is_broken + 1] = False

if min_count == 10 ** 6:
    print(-1)
else:
    print(min_count)