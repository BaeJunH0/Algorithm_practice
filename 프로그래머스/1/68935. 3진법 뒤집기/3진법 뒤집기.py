def tri(n):
    tri = ''
    while n >= 3:
        tri += str(n % 3)
        n //= 3
    tri += str(n)
    return tri[::-1]
def solution(n):
    answer = 0
    temp = tri(n)
    num = 1
    for i in temp:
        answer += num * int(i)
        num *= 3
    return answer