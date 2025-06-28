import heapq

def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap)
    
    answer = 0
    while heap:
        if heap[0] >= K:
            break
        if len(heap) == 1:
            return -1
        
        temp = heapq.heappop(heap) + 2 * heapq.heappop(heap)
        heapq.heappush(heap, temp)
        answer += 1
        
    
    return answer