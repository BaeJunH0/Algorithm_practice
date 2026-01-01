import sys
input = sys.stdin.readline

number = int(input())

while number % 2 == 0:
    number = number // 2

if number != 1:
    print(0)
else:
    print(1)