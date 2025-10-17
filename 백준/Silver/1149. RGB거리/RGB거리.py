import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
rgb = []

for i in range(T):
    rgb.append(list(map(int, input().rstrip().split())))

dp = [[0] * 3 for _ in range(T)]
dp[0] = rgb[0]

for i in range(1, T):
    dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))