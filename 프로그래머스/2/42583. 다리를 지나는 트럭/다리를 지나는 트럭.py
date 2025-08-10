from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    
    now_weight = 0
    count = 0
    
    while truck:
        count += 1
        now_weight -= bridge.popleft()
        
        now = 0
        
        if now_weight + truck[0] <= weight:
            now = truck.popleft()
        bridge.append(now)
        
        now_weight += now
    
    count += len(bridge)
    
    return count