import sys

input = sys.stdin.readline

N = int(input())
Pn = 'I' + 'OI' * N

seq = int(input())
string = input().rstrip()

answer = 0
for i in range(0, seq - len(Pn) + 1):
    count = 0
    for j in range(0, len(Pn)):
        if string[i + j] != Pn[j]:
            break
        count += 1
    
    if count == len(Pn):
        answer += 1

print(answer)