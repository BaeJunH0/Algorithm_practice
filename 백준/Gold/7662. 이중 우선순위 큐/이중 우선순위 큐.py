import sys, heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    seq = int(input())
    visited = [False] * seq
    min_heap, max_heap = [], []
    for i in range(seq):
        command, num = input().rstrip().split()
        num = int(num)

        # 삽입
        if command == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        # 최대 값 삭제
        elif num == 1:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        # 최소 값 삭제
        else:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    print(-max_heap[0][0], min_heap[0][0]) if max_heap and min_heap else print('EMPTY')