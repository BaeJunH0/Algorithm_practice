import sys

input = sys.stdin.readline

n = int(input())

arr = [0, 1, 2, 3]

for i in range(4, n + 1):
    arr.append(arr[i-2] + arr[i-1])

print(arr[n] % 10007)