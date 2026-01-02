import sys

input = sys.stdin.readline

number = int(input())

while True:
    oper = input().rstrip()
    if oper == '=':
        print(number)
        break
        
    temp = int(input())
    if oper == '+':
        number += temp
    elif oper == '-':
        number -= temp
    elif oper == '*':
        number *= temp
    else:
        number //= temp