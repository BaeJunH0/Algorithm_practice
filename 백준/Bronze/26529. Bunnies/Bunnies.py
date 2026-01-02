import sys

input = sys.stdin.readline

dp = [1, 1] + [0] * 44

for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]

seq = int(input())

for _ in range(seq):
    number = int(input())
    print(dp[number])