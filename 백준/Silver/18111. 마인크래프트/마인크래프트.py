import sys

input = sys.stdin.readline

n, m, b = map(int, input().rstrip().split())

line = []
for i in range(n):
    input_line = list(map(int, input().rstrip().split()))
    line += input_line

line.sort(reverse = True)

answer = 500 * 500 * 256
depth = 0
for i in range(256 + 1):
    small_value = 0
    big_value = 0

    for j in line:
        if i < j:
            big_value += j - i
        elif i > j:
            small_value += i - j
    
    if b + big_value < small_value:
        continue
    
    if answer >= big_value * 2 + small_value:
        answer = big_value * 2 + small_value
        depth = i

print(answer, depth)