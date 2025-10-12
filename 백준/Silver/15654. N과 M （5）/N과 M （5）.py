import sys

input = sys.stdin.readline

def backtracking():
    if len(case) == m:
        for i in case:
            print(i, end=" ")
        print()
    for i in numbers:
        if i not in case:
            case.append(i)
            backtracking()
            case.pop()


n, m = list(map(int, input().split()))

numbers = list(map(int, input().split()))
numbers.sort()

case = []

backtracking()