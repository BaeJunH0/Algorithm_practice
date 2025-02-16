def fac(n):
    ret = 1
    if n == 0 or n == 1:
        return ret
    for i in range(2, n + 1):
        ret *= i
    return ret

def solution(n):
    answer = 0
    temp = n // 2
    
    # i = 2의 개수
    for i in range(temp + 1):
        one = n - i * 2
        two = i
        answer += fac(one + two) // fac(one) // fac(two)
    return answer % 1234567