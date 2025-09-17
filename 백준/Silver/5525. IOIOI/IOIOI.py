import sys

input = sys.stdin.readline

N = int(input())
Pn = 'I' + 'OI' * N

seq = int(input())
string = input().rstrip()
size = len(Pn)

answer = 0
count = 0
i = 0
while i < seq - 1:
    if string[i:i+3] == "IOI":
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)