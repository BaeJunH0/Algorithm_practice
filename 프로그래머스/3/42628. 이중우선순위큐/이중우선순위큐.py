import heapq

def solution(operations):
    heap = []
    
    for i in operations:
        command, number = i.split(' ')
        if command == 'I':
            heap.append(int(number))
        if command == 'D' and heap:
            if number == '-1':
                heapq.heapify(heap)
                heapq.heappop(heap)
            else:
                heap = [-1 * x for x in heap]
                heapq.heapify(heap)
                heapq.heappop(heap)
                heap = [-1 * x for x in heap]
    
    if heap:
        return [max(heap), min(heap)]
    
    return [0, 0]