import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().rstrip().split())

arr = [[''] * col for _ in range(row)]

start = [0, 0]

for i in range(row):
    string = input().rstrip()

    for j in range(col):
        arr[i][j] = string[j]
        if string[j] == 'I':
            start[0], start[1] = i, j

queue = deque()
queue.append(start)
arr[start[0]][start[1]] = 'X'

dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]

answer = 0
while queue:
    target = queue.popleft()

    for i in dir:
        nrow, ncol = target[0] + i[0], target[1] + i[1]
        if 0 <= nrow < row and 0 <= ncol < col and arr[nrow][ncol] != 'X':
            if arr[nrow][ncol]  == 'P':
                answer += 1
            arr[nrow][ncol] = 'X'
            queue.append([nrow, ncol])

print(answer if answer != 0 else 'TT')