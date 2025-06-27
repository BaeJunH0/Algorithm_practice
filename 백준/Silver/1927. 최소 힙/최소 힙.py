import heapq
import sys

input = sys.stdin.readline

heap = []
heapq.heapify(heap)

seq = int(input())
for i in range(seq):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
    