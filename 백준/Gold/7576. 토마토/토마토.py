import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().rstrip().split())
arr = [[] for _ in range(col)]

for i in range(col):
    arr[i] = list(map(int, input().rstrip().split()))


check_list = []
for i in range(col):
    for j in range(row):
        if arr[i][j] == 1:
            check_list.append([i, j])

queue = deque()
direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]

for i in check_list:
    queue.append(i)

answer = 0
while queue:
    seq = len(queue)

    for i in range(seq):
        n_col, n_row = queue.popleft()
        for x, y in direction:
            if 0 <= n_col + x < col and 0 <= n_row + y < row and arr[n_col + x][n_row + y] == 0:
                arr[n_col + x][n_row + y] = 1
                queue.append([n_col + x, n_row + y])
    answer += 1

for i in range(col):
    for j in range(row):
        if arr[i][j] == 0:
            print(-1)
            exit()

print(answer - 1)