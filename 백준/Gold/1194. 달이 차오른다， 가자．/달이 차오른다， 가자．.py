# 달이 차오른다 가자
import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().rstrip().split())

arr = []
start = [0, 0]

for i in range(row):
    line = input().rstrip()
    temp = []

    for j in range(col):
        if line[j] == '0':
            start = [i, j]
            temp.append('.')
        else:
            temp.append(line[j])

    arr.append(temp)

def bfs(a, b):
    queue = deque()
    dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]
    queue.append([a, b, 0, 0])
    visited = [[[False] * (1 << 6) for _ in range(col)] for _ in range(row)]
     
    while queue:
        x, y, count, key = queue.popleft()

        for r, c in dir:
            n_row, n_col, n_count = r + x, c + y, count + 1

            if 0 <= n_row < row and 0 <= n_col < col and not visited[n_row][n_col][key]:
                if arr[n_row][n_col] == '1':
                    return n_count
                elif arr[n_row][n_col] == '.':
                    visited[n_row][n_col][key] = 1
                    queue.append([n_row, n_col, n_count, key])
                elif 'a' <= arr[n_row][n_col] <= 'f':
                    n_key = key | (1 << (ord(arr[n_row][n_col]) - ord('a')))
                    visited[n_row][n_col][n_key] = 1
                    queue.append([n_row, n_col, n_count, n_key])
                elif 'A' <= arr[n_row][n_col] <= 'F':
                    if bool(key & (1 << (ord(arr[n_row][n_col]) - ord('A')))):
                        visited[n_row][n_col][key] = 1
                        queue.append([n_row, n_col, n_count, key])
                
    return -1
print(bfs(start[0], start[1]))