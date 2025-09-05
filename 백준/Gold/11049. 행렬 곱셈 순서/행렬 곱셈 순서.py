# https://www.acmicpc.net/problem/11049
# 행렬 곱셈 순서

import sys

input = sys.stdin.readline

seq = int(input())

def calculate(a, b):
    return a[0] * a[1] * b[1]

arr = [list(map(int, input().rstrip().split())) for _ in range(seq)]
dp = [[0] * seq for _ in range(seq)]

for i in range(1, seq): # i = 간격
    for j in range(0, seq - i): # j = 계산 시작점
    
        if i == 1: # 바로 다음까지이므로 그냥 행렬곱
            dp[j][j+i] = arr[j][0] * arr[j][1] * arr[j+i][1]
            continue
        
        dp[j][j+i] = 2**31 # 문제 조건상 나올 수 없는 최대 값

        for k in range(j, j+i): # k = 분기점
            # 경우의 수 계산 -> ex) 1~3 이면 (1 + 2) + 3 or 1 + (2 + 3) 선정 로직
            # dp[j][k] = j ~ k 까지의 최소 계산 값
            # dp[k+1][j+i] = k+1 ~ j+i까지의 최소 계산 값
            # arr[j][0] * arr[k][1] * arr[j+i][1] = 계산 시 추가 발생 비용
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0] * arr[k][1] * arr[j+i][1])

print(dp[0][-1])
