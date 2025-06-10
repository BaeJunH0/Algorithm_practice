import sys

input = sys.stdin.readline

seq = int(input())

for _ in range(seq):
    dic = {}
    val = int(input())
    for i in range(val):
        a, b = input().strip().split()
        if b not in dic.keys():
            dic[b] = [a]
        else:
            dic[b].append(a)
    
    target = map(len, dic.values())
    response = 1
    for i in target:
        response *= i + 1
    print(response - 1)