import sys, heapq

INF = sys.maxsize
input = sys.stdin.readline

seq = int(input())

for _ in range(seq):
    v, e, start = map(int, input().rstrip().split())

    adj = [[] for __ in range(v + 1)]
    for i in range(e):
        a, b, s = map(int, input().rstrip().split())

        adj[b].append((s, a))

    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (v + 1)
    distance[start] = 0

    while heap:
        weight, target = heapq.heappop(heap)

        if distance[target] < weight:
            continue

        for nw, nt in adj[target]:
            cost = weight + nw
            if distance[nt] > cost:
                distance[nt] = cost

                heapq.heappush(heap, (cost, nt))
    
    cnt = 0
    max_time = -1
    for i in distance:
        if i != INF:
            cnt += 1

            if max_time < i:
                max_time = i
    
    print(cnt, max_time)