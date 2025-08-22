import sys

input = sys.stdin.readline

num = int(input())
dp = [0] * (num + 1)

step = 1
while step ** 2 <= num:
    dp[step ** 2] = 1
    step += 1

for i in range(1, num + 1):
    if dp[i] != 0:
        continue
    
    j = 1
    while j ** 2 <= i:
        if dp[i] == 0:
            dp[i] = dp[j*j] + dp[i - j*j]
        else:
            dp[i] = dp[i] if dp[i] < dp[j*j] + dp[i - j*j] else dp[j*j] + dp[i - j*j]
        j += 1

print(dp[num])