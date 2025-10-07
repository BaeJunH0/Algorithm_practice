import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().rstrip().split())

field = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, w = map(int, input().rstrip().split())

    field[a].append((w, b))
    field[b].append((w, a))

must = list(map(int, input().rstrip().split()))
search_set = set([1] + must)

distances = {}
for i in search_set:
    heap = []
    heapq.heappush(heap, (0, i))
    distance = [INF] * (v + 1)
    distance[i] = 0

    while heap:
        weight, target = heapq.heappop(heap)

        if distance[target] < weight:
            continue

        for nw, nt in field[target]:
            cost = nw + distance[target]
            if distance[nt] > cost:
                distance[nt] = cost
                heapq.heappush(heap, (cost, nt))
    
    distances[i] = distance

v1 = distances[1][must[0]] + distances[must[0]][must[1]] + distances[must[1]][v]
v2 = distances[1][must[1]] + distances[must[1]][must[0]] + distances[must[0]][v]

if min(v1, v2) >= INF:
    print(-1)
else:
    print(min(v1, v2))