import sys
from collections import deque

input = sys.stdin.readline

max_seq = int(input())

col, row = map(int, map(int, input().rstrip().split()))

field = []

for i in range(row):
    field.append(list(map(int, input().rstrip().split())))

check = [[[False] * (max_seq + 1) for _ in range(col)] for _ in range(row)]
queue = deque([(0, 0, 0, 0)])
check[0][0][0] = True

normal_dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
extra_dir = [(-1, 2), (-2, 1), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

min_count = 40001
while queue:
    x, y, used, count = queue.popleft()

    if x == row - 1 and y == col - 1:
        min_count = min(min_count, count)
    
    for a, b in normal_dir:
        nx, ny = x + a, y + b
        if 0 <= nx < row and 0 <= ny < col and field[nx][ny] != 1:
            if not check[nx][ny][used]:
                queue.append((nx, ny, used, count + 1))
                check[nx][ny][used] = True
    
    for a, b in extra_dir:
        nx, ny = x + a, y + b
        if 0 <= nx < row and 0 <= ny < col and field[nx][ny] != 1:
            if used < max_seq and not check[nx][ny][used + 1]:
                queue.append((nx, ny, used + 1, count + 1))
                check[nx][ny][used + 1] = True

print(min_count if min_count != 40001 else -1)