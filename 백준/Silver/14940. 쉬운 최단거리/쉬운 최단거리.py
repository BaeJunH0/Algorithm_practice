import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().rstrip().split())

zido = [list(map(int, input().rstrip().split())) for _ in range(row)]
check = [[-1] * col for _ in range(row) ]

start = [0, 0]

for i in range(row):
    for j in range(col):
        if zido[i][j] == 2:
            start = [i, j]

queue = deque()
dis = [[0, 1], [-1, 0], [0, -1], [1, 0]]

check[start[0]][start[1]] = 0
queue.append(start)

while queue:
    now_row, now_col = queue.popleft()

    for i in dis:
        next_row = now_row + i[0]
        next_col = now_col + i[1]

        if 0 <= next_row < row and 0 <= next_col < col and check[next_row][next_col] == -1:
            if zido[next_row][next_col] == 0:
                check[next_row][next_col] = 0
            elif zido[next_row][next_col] == 1:
                check[next_row][next_col] = check[now_row][now_col] + 1
                queue.append([next_row, next_col])


# 정답 출력
for i in range(row):
    for j in range(col):
        if zido[i][j] == 0:
            print(0, end = ' ')
        else:
            print(check[i][j], end = ' ')
    print()