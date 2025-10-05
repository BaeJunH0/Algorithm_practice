import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
INF = sys.maxsize

start = int(input())

adj = [{i : 0} for i in range(V + 1)]
    
for _ in range(E):
    a, b, w = map(int, input().rstrip().split())

    if b not in adj[a].keys():
        adj[a][b] = w
    else:
        adj[a][b] = min(adj[a][b], w)

distance = [INF] * (V + 1)
heap = []
heapq.heappush(heap, (0, start))
distance[start] = 0

while heap:
    weight, target = heapq.heappop(heap)

    if weight > distance[target]:
        continue

    for i in adj[target].keys():
        cost = weight + adj[target][i]
        if distance[i] > cost:
            distance[i] = cost
            heapq.heappush(heap, (cost, i))

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i]) 
