import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

graph = {}
for _ in range(T-1):
    a, b = map(int, input().rstrip().split())

    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)

queue = deque()
queue.append(1)
visited = [False] * (T + 1)
visited[1] = True
parent = [None] * (T + 1)

while queue:
    target = queue.popleft()

    for i in graph[target]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            parent[i] = target

for i in range(2, T + 1):
    print(parent[i])