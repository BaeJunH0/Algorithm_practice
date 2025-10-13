# 가장 긴 증가하는 수열 - dp

import sys

input = sys.stdin.readline

T = int(input())
dp = [1] * T
seq = list(map(int, input().rstrip().split()))

for i in range(1, T):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))