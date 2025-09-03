import sys

input = sys.stdin.readline


seq = int(input())

# 문제 조건 : k일이 걸리는 일과 보수
scedule = [[]]

# n일차까지 얻을 수 있는 최대 보상
dp = [0] * (seq + 1)
for _ in range(seq):
    scedule.append(list(map(int, input().rstrip().split())))

for i in range(1, seq + 1):
    scedule[i][0] += i - 1

now_max = 0
for i in range(1, seq + 1):
    day, value = scedule[i]

    # 이전 최대 값 반영
    dp[i] = max(now_max, dp[i])

    if day <= seq:
        # 오늘 일을 시작하는게 이득인지 판단
        # 해당 날에 보수를 받는다면 -> 이전 날까지의 최대 보수 + 지금 보수 or 기존 오늘의 최대 보수
        # dp[day] 가 더 크다면 : 기존 최대 보수가 더 크므로 해당 선택
        # dp[day-1] + value 가 더 크다면 : 이전 날까지의 최대 보수 + i번째 날에 일해서 day에 받는게 더 크므로 해당 선택
        dp[day] = max(dp[day], dp[i-1] + value)

    now_max = dp[i]

print(dp[-1])