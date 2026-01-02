import sys

input = sys.stdin.readline

string = input().rstrip()

if '(' in string:
    idx = 0
    while string[idx] != '(':
        idx += 1
    
    print(string[:idx])
    print(string[idx+1:-1])
else:
    print(string)
    print('-')