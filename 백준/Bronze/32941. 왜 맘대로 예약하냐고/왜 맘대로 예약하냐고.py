import sys

input = sys.stdin.readline

a, gunwoo = map(int, input().rstrip().split())

seq = int(input())

for _ in range(seq):
    count = int(input())
    arr = map(int, input().rstrip().split())

    if gunwoo not in arr:
        print('NO')
        exit()

print('YES')