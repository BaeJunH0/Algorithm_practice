import sys
import math

input = sys.stdin.readline

size = int(input().rstrip())

max_two = size // 2

answer = 0
for i in range(0, max_two + 1):
    num_two = i
    num_one = size - i * 2
    now_size = num_one + num_two

    add_one = math.factorial(now_size) // (math.factorial(num_one) * math.factorial(num_two))

    boot = 2 ** i
    answer += add_one * boot
        

print(answer % 10007)
