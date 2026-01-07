# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

input = sys.stdin.readline

# dfs
def dfs(st : int) -> None:
    dfs_visited[st] = 1

    print(st, end = ' ')

    target = al[st]
    for i in target:
        if dfs_visited[i] == 0:
            dfs(i)

# bfs
def bfs(st : int) -> None:
    queue = deque()
    queue.append(st)
    bfs_visited[st] = 1

    while queue:
        target = queue.popleft()

        print(target, end = ' ')

        for i in al[target]:
            if bfs_visited[i] == 0:
                bfs_visited[i] = 1
                queue.append(i)

# main
v, e, start = map(int, input().rstrip().split())

# 탐색 중 정점 방문 여부 저장
dfs_visited = [0] * (v + 1)
bfs_visited = [0] * (v + 1)

# 인접 리스트 선언
al = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().rstrip().split())

    al[a].append(b)
    al[b].append(a)

for i in range(1, v + 1):
    al[i].sort()

dfs(start)
print()
bfs(start)