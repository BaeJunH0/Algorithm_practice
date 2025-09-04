# https://www.acmicpc.net/problem/1520
# 내리막 길

import sys

sys.setrecursionlimit (10**9)
input = sys.stdin.readline

row, col = map(int, input().rstrip().split())

h_map = [list(map(int, input().rstrip().split())) for _ in range(row)]
dp = [[-1] * col for _ in range(row)]

dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]

def finding(x, y):
    # 재귀 끝 조건
    if x == row - 1 and y == col -1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for tx, ty in dir:
            nextx, nexty = x + tx, y + ty 
            if 0 <= nextx < row and 0 <= nexty < col and h_map[nextx][nexty] < h_map[x][y]:
                dp[x][y] += finding(nextx, nexty)
    
    return dp[x][y]

print(finding(0, 0))