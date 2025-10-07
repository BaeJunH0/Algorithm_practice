import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

v, e, k, start = map(int, input().rstrip().split())

field = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().rstrip().split())
    field[a].append((1, b))

heap = []
heapq.heappush(heap, (0, start))
distance = [INF] * (v + 1)
distance[start] = 0

while heap:
    weight, target = heapq.heappop(heap)

    if distance[target] < weight:
        continue

    for nw, nt in field[target]:
        cost = nw + distance[target]
        if distance[nt] > cost:
            distance[nt] = cost
            heapq.heappush(heap, (cost, nt))

checksum = True
for i in range(1, v + 1):
    if distance[i] == k:
        print(i)
        checksum = False

if checksum:
    print(-1)