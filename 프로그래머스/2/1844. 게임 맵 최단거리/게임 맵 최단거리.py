from collections import deque

def solution(maps):
    index = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    answer = -1
    xmax = len(maps) - 1
    ymax = len(maps[0]) - 1
    
    arr = [[0, 0, 1]]
    maps[0][0] = 0
    
    deq = deque(arr)
    
    while len(deq) != 0:
        # dequeue
        now = deq.popleft()
        
        # 순회 과정 ( 상 하 좌 우 )
        for i in index:
            # 다음 노드 세팅
            nextx = now[0] + i[0]
            nexty = now[1] + i[1]
            
            # 다음 노드의 위치가 maps 범위 밖이면 방문 x
            if nextx < 0 or nextx > xmax or nexty < 0 or nexty > ymax:
                continue
                
            # 다음 노드가 벽 (0) 이면 방문 x
            if maps[nextx][nexty] == 0:
                continue
                
            # 종료 판정
            if nextx == xmax and nexty == ymax:
                return now[2] + 1
            
            # 다음 노드 추가
            deq.append([nextx, nexty, now[2] + 1])
            
            # 방문하기로 한 노드는 다른 순간에 추가하지 못하게 함
            maps[nextx][nexty] = 0
    return -1