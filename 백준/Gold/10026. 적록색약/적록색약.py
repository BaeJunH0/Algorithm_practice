import sys
from collections import deque

input = sys.stdin.readline

def normal_bfs(alphabet):
    while normal_queue:
        x, y = normal_queue.popleft()

        for a, b in dir:
            nx, ny = x + a, y + b
            if 0 <= nx < seq and 0 <= ny < seq and not normal_check[nx][ny]:
                if normal[nx][ny] == alphabet:
                    normal_queue.append((nx, ny))
                    normal_check[nx][ny] = True

def abnormal_bfs(alphabet):
    while abnormal_queue:
        x, y = abnormal_queue.popleft()

        for a, b in dir:
            nx, ny = x + a, y + b
            if 0 <= nx < seq and 0 <= ny < seq and not abnormal_check[nx][ny]:
                if abnormal[nx][ny] == alphabet:
                    abnormal_queue.append((nx, ny))
                    abnormal_check[nx][ny] = True



seq = int(input())

normal, abnormal = [], []
normal_check, abnormal_check = [[False] * seq for _ in range(seq)], [[False] * seq for _ in range(seq)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(seq):
    normal_line = []
    abnormal_line = []

    for i in input().rstrip():
        if i == 'G':
            normal_line.append('G')
            abnormal_line.append('R')
        else:
            normal_line.append(i)
            abnormal_line.append(i)
    
    normal.append(normal_line)
    abnormal.append(abnormal_line)

normal_queue = deque()
abnormal_queue = deque()

normal_count , abnormal_count = 0, 0
for i in range(seq):
    for j in range(seq):
        if not normal_check[i][j]:
            normal_check[i][j] = True
            normal_queue.append((i,j))
            normal_bfs(normal[i][j])
            normal_count += 1
        if not abnormal_check[i][j]:
            abnormal_check[i][j] = True
            abnormal_queue.append((i,j))
            abnormal_bfs(abnormal[i][j])
            abnormal_count += 1

print(normal_count, abnormal_count)