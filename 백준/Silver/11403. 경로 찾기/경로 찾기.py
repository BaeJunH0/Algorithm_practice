import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
adj = []
response = [[0] * N for _ in range(N)]

for i in range(N):
    adj.append(list(map(int, input().rstrip().split())))

for i in range(N):
    visited = [0] * N
    queue = deque()

    for j in range(N):
        if adj[i][j] == 1:
            queue.append(j)
            visited[j] = 1

    while queue:
        target = queue.popleft()
        response[i][target] = 1

        for j in range(N):
            if adj[target][j] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] = 1

for i in response:
    for j in i:
        print(j, end = ' ')
    print()