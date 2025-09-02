# https://www.acmicpc.net/problem/11066
# 파일 합치기

import sys

input = sys.stdin.readline

seq = int(input())

def knuth(number):
    dp = [[0] * (number + 1) for _ in range(number + 1)]
    sum = [0] * (number + 1)

    count = 1
    for i in list(map(int, input().rstrip().split())):
        sum[count] = sum[count-1] + i
        count += 1

    # i = 파일 선택 개수 (1 ~ number-1 개)
    # start = 인덱스 스타팅 포인트 (1 ~ number-i)
    # k = 중간 지점 (start ~ start + i - 1)
    for i in range(1, number):
        for start in range(1, number - i + 1):
            end = start + i

            min_num = min([dp[start][k] + dp[k+1][end] for k in range(start, end)])
            
            dp[start][end] = min_num + sum[end] - sum[start - 1]

    print(dp[1][number])
            
        
for _ in range(seq):
    number = int(input())
    knuth(number)