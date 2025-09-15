import sys
from collections import deque

input = sys.stdin.readline

seq = int(input())

answer_map = [[-1] * seq for _ in range(seq)]
arr = []

for i in range(seq):
    line = input().rstrip()
    temp = []

    for j in line:
        temp.append(int(j))
    
    arr.append(temp)

queue = deque()
dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]
answer = []

for i in range(seq):
    for j in range(seq):
        if arr[i][j] == 1 and answer_map[i][j] == -1:
            count = 1
            queue.append([i, j])
            answer_map[i][j] = 0

            while queue:
                a, b = queue.popleft()

                for r, c in dir:
                    n_row, n_col = r + a, c + b

                    if 0 <= n_row < seq and 0 <= n_col < seq and arr[n_row][n_col] == 1 and answer_map[n_row][n_col] == -1:
                        queue.append([n_row, n_col])
                        answer_map[n_row][n_col] = 0
                        count += 1

            answer.append(count)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
