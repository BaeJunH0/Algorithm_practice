# 점화식 찾기
# dp[1] = 1
# dp[2] = 2 <- 1+1, 2
# dp[3] = 4 <- 1+1+1, 2+1, 1+2, 3
# dp[4] = 7 <- 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1 <- dp[1] + dp[2] + dp[3]
# dp[5] = 13
# dp[6] = 24
# dp[7] = 44 ...
import sys

input = sys.stdin.readline

seq = int(input())

dp = [0, 1, 2, 4] + [0] * 8

# 범위 = 11까지
for i in range(4, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1] 

for i in range(seq):
    test = int(input())
    print(dp[test])
