import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

v, m, e = map(int, input().rstrip().split())

item = [0] + list(map(int, input().rstrip().split()))

field = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, w = map(int, input().rstrip().split())

    field[a].append((w, b))
    field[b].append((w, a))

item_max = -1
for i in range(1, v + 1):
    start = i

    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (v + 1)
    distance[start] = 0

    while heap:
        weight, target = heapq.heappop(heap)

        if distance[target] < weight:
            continue

        for nw, nt in field[target]:
            cost = weight + nw
            if distance[nt] > cost:
                distance[nt] = cost
                
                heapq.heappush(heap, (cost, nt))
    
    sum_num = 0
    for j in range(1, v + 1):
        if distance[j] <= m:
            sum_num += item[j]
    
    if sum_num > item_max:
        item_max = sum_num

print(item_max)