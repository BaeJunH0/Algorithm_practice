import sys

input = sys.stdin.readline

T = int(input())
dp = [[0] * T for _ in range(T)] 

for i in range(T):
    temp = list(map(int, input().rstrip().split()))
    for j in range(len(temp)):
        dp[i][j] = temp[j]

for i in range(1, T):
    for j in range(i + 1):
        left, right = j - 1, j
        if left < 0:
            dp[i][j] += dp[i-1][right]
        elif 0 <= left and right < i:
            dp[i][j] += max(dp[i-1][left], dp[i-1][right])
        else:
            dp[i][j] += dp[i-1][left]

print(max(dp[-1]))
