import sys
input = sys.stdin.readline

seq = int(input().rstrip())
# i번째 계단까지 점수의 최대 값
value = [0 for i in range(301)]
for i in range(1, seq+1):
    value[i] = int(input().rstrip())

# dp[1] = 첫번째 계단까지의 최대값
dp = [0 for i in range(301)]
dp[1] = value[1]
dp[2] = value[2] + value[1]
dp[3] = max(value[1] + value[3], value[2] + value[3])

for i in range(4, seq + 1):
    dp[i] = max(dp[i-2] + value[i], dp[i-3] + value[i-1] + value[i])


print(dp[seq])