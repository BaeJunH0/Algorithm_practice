from collections import deque

def solution(priorities, location):
    priority_queue = deque(priorities)
    location_queue = deque([x for x in range(len(priorities))])
    
    count = 0
    while True:
        temp_p = priority_queue.popleft()
        temp_l = location_queue.popleft()
        
        checksum = 0
        for i in priority_queue:
            if temp_p < i:
                checksum = 1
                break
                
        if checksum == 1:
            priority_queue.append(temp_p)
            location_queue.append(temp_l)
        else:
            count += 1
            if temp_l == location:
                return count