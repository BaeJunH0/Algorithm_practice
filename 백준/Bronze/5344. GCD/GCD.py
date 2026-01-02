import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

seq = int(input())

for _ in range(seq):
    a, b = map(int, input().rstrip().split())
    print(gcd(a, b))
