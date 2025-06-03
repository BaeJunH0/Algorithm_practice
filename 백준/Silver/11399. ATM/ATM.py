seq = int(input())

line = list(map(int, input().split()))
line.sort()

answer = 0
for i in range(1, seq):
    line[i] += line[i-1]

print(sum(line))