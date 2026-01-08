# https://www.acmicpc.net/problem/1012

import sys
from collections import deque

input = sys.stdin.readline

def simulation():
    row, col, value = map(int, input().rstrip().split())

    # 배추밭
    baechu = [[0] * col for _ in range(row)]

    # 방문 여부
    visited = [[0] * col for _ in range(row)]

    # 배추 위치
    target = []
    for _ in range(value):
        x, y = map(int, input().rstrip().split())
        baechu[x][y] = 1

        target.append((x, y))
    
    # 구역 나누기 (인접한 1은 하나의 무리로 봄)
    count = 0
    for a, b in target:
        if visited[a][b] == 1:
            continue

        queue = deque()
        queue.append((a, b))
        visited[a][b] = 1

        direction = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        while queue:
            x, y = queue.popleft()

            for c, d in direction:
                nx, ny = x + c, y + d

                if 0 <= nx < row and 0 <= ny < col and baechu[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

        count += 1
        
    print(count)

# Test case의 개수, 시뮬레이션 느낌으로 가는 거
seq = int(input())

# main에서 안하고 깔끔하게 돌리기
for _ in range(seq):
    simulation()