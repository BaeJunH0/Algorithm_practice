import sys

input = sys.stdin.readline

# 작업의 개수
seq = int(input())

# 선행 작업 관계
sunhang = [[] for _ in range(seq)]

# 작업이 걸리는 시간
task = [0 for _ in range(seq)]

# 작업 받기
for i in range(seq):
    task_command = list(map(int, input().rstrip().split()))

    for j in range(2, 2 + task_command[1]):
        sunhang[i].append(task_command[j] - 1)

    task[i] = task_command[0]

dp = [0 for _ in range(seq)]

for i in range(seq):
    wait_time = 0

    for j in sunhang[i]:
        if wait_time < dp[j]:
            wait_time = dp[j]

    dp[i] = wait_time + task[i]

print(max(dp))