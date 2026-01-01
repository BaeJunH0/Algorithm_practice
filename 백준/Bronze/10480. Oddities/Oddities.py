import sys

input = sys.stdin.readline

seq = int(input())

for _ in range(seq):
    temp = int(input())

    if temp % 2 == 0:
        print(temp, 'is even')
    else:
        print(temp, 'is odd')