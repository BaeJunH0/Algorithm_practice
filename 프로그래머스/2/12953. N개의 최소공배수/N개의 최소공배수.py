def solution(arr):
    answer = 1
    for i in arr:
        answer = lcm(i, answer)
    return answer

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)