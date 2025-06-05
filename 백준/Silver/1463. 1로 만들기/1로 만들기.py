number = int(input())

# N의 최대 값이 10^6
dp = [0 for i in range(1000001)]

# DP 사용
# dp[i]의 의미 : i에서 1까지 가는 연산의 최소 값
# dp[2] 부터 확인 -> dp[1]은 1에서 1까지 가는 연산의 최소 값 == 0
# dp[number] 까지 확인 -> 결국 원하는 정답 = dp[number]이 얼마인지 구하는 것
for i in range(2, number + 1):
    # 1을 빼는 연산
    dp[i] = dp[i-1] + 1
    # 2로 나누는 연산 ( i가 2로 나누어 떨어질 때 )
    if i % 2 == 0:
        # 이전 단계의 연산 최소 값을 비교
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3으로 나누는 연산 ( i가 3으로 나누어 떨어질 때 )
    if i % 3 == 0:
        # 이전 단계의 연산 최소 값을 비교
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[number])