import sys

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().rstrip().split())

graph = []

for _ in range(e):
    a, b, w = map(int, input().rstrip().split())

    graph.append((a, b, w))

distance = [INF] * (v + 1)
distance[1] = 0

for i in range(v):
    for j in range(e):
        cur_node, next_node, weight = graph[j]

        if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + weight:
            distance[next_node] = distance[cur_node] + weight

            if i == v - 1:
                print(-1)
                exit()

for i in range(2, v + 1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print(-1)
