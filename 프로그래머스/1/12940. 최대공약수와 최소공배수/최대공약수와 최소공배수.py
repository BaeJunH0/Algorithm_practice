def lcm(a, b):
    return (a * b) // gcd(a, b)
def gcd(a, b):
    temp = 0
    if a < b:
        temp = a
        a = b
        b = temp
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a
def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer