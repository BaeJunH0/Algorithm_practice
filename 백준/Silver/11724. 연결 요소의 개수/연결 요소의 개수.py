import sys
from collections import deque

input = sys.stdin.readline

def bfs(num, graph, visited):
    queue = deque()
    queue.append(num)
    visited[num] = 1

    while queue:
        now = queue.popleft()
        targets = graph[now]

        for target in targets:
            if visited[target] == 0:
                queue.append(target)
                visited[target] = 1

    return visited

node, edge = map(int, input().rstrip().split())

graph = [[] for _ in range(node + 1)]

for i in range(edge):
    a, b = map(int, input().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (node + 1)

answer = 0
for i in range(1, node + 1):
    if visited[i] == 0:
        if not graph[i]:
            visited[i] = 1
            answer += 1
        else:
            visited = bfs(i, graph, visited)
            answer += 1

print(answer)