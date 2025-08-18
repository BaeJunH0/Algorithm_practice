import sys

input = sys.stdin.readline

seq = int(input().rstrip())

if seq == 0:
    print(0)
    exit()

arr = []
for i in range(seq):
    arr.append(list(map(int, input().rstrip().split())))

arr.sort(key = lambda x : (x[1], x[0]))

last = 0
answer = 0

for element in arr:
    if element[0] >= last:
        answer += 1
        last = element[1]

print(answer)