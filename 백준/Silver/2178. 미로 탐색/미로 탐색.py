import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().rstrip().split())

answer_map = [[-1] * col for _ in range(row)]
arr = []

for i in range(row):
    line = input().rstrip()
    temp = []

    for l in line:
        temp.append(int(l))
    
    arr.append(temp)

queue = deque()
queue.append([0, 0, 1])
answer_map[0][0] = 1


dic = [[0, 1], [1, 0], [-1, 0], [0, -1]]

while queue:
    a, b, count = queue.popleft()

    for r, c in dic:
        n_row, n_col, n_count = a + r, b + c, count + 1

        if 0 <= n_row < row and 0 <= n_col < col and arr[n_row][n_col] == 1 and answer_map[n_row][n_col] == -1:
            queue.append([n_row, n_col, n_count])
            answer_map[n_row][n_col] = n_count

print(answer_map[row-1][col-1])