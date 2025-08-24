import sys

input = sys.stdin.readline

inline = input().rstrip()

operators = []
numbers = []

temp = ''
for i in inline:
    if not i.isdigit():
        operators.append(i)
        numbers.append(int(temp))
        temp = ''
    else:
        temp += i
        
if temp != '':
    numbers.append(int(temp))

# 숫자 하나만 나올 때
if len(operators) == 0:
    print(numbers[0])
    exit()

# '-'가 있을 때
for i in range(len(operators)):
    if operators[i] == '-':
        print(sum(numbers[:i+1]) - sum(numbers[i+1:]))
        exit()

# '+'만 있을 때
print(sum(numbers))