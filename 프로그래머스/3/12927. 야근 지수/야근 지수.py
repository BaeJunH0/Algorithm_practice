import heapq

def solution(n, works):
    if sum(works) - n <= 0:
        return 0
    
    # 최대 힙
    heap = [-x for x in works]
    heapq.heapify(heap)
    
    for _ in range(n):
        max_num = heapq.heappop(heap)
        max_num += 1
        heapq.heappush(heap, max_num)
        
    return sum([x**2 for x in heap])