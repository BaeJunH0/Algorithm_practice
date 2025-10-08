import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

def bfs(start, end):
    queue = deque([start])
    visited = [False] * (v)
    visited[start] = True

    while queue:
        now = queue.popleft()

        if now == end:
            return True

        for s, e, w in graph:
            if now == s and not visited[e]:
                queue.append(e)
                visited[e] = True

    return False

v, start, end, e = map(int, input().rstrip().split())

graph = []

for _ in range(e):
    a, b, cost = map(int, input().rstrip().split())
    graph.append([a, b, cost])

pay = list(map(int, input().rstrip().split()))

for i in range(e):
    graph[i][2] = pay[graph[i][1]] - graph[i][2]

distance = [-INF] * v
distance[start] = pay[start]

# v-1번 수행 -> 양수 사이클 여부 확인만 제외
for _ in range(v - 1):
    for j in range(e):
        cur, nxt, cost = graph[j]
        if distance[cur] != -INF and distance[nxt] < distance[cur] + cost:
            distance[nxt] = distance[cur] + cost

# 양수 사이클 여부 확인
is_cycle = False
for i in range(e):
    cur, nxt, cost = graph[i]

    if distance[cur] != -INF and distance[nxt] < distance[cur] + cost:
        if bfs(nxt, end):
            is_cycle = True
            break

if distance[end] == -INF:
    print('gg')
else:
    if is_cycle:
        print('Gee')
    else:
        print(distance[end])