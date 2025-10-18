import sys

input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())

def devide_and_quenquer(a, b, c):
    if b == 1:
        return a % c
    
    nxt = devide_and_quenquer(a, b // 2, c)

    if b % 2 == 0:
        return (nxt * nxt) % c
    else:
        return (nxt * nxt * a) % c

print(devide_and_quenquer(a, b, c))