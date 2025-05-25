# https://www.acmicpc.net/problem/24511

a = int(input())
arr = list(map(int, input().split()))
past_values = list(map(int, input().split()))
b = int(input())
insert_values = list(map(int, input().split()))

answer = []

for i in range(len(arr)):
    if arr[i] == 0:
        answer.append(past_values[i])

answer = answer[::-1] + insert_values

for i in answer[:len(insert_values)]:
    print(i, end = ' ')