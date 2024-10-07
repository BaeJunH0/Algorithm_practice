def check(a, b):
    a_temp = str(bin(a))
    b_temp = str(bin(b))
    diff = 0
    if len(b_temp) > len(a_temp):
        diff = len(b_temp) - len(a_temp)
    a_temp += '0' * diff
    if sorted(a_temp) !=  sorted(b_temp):
        return False
    return True
def solution(n):
    answer = n + 1
    while not check(n, answer):
        answer += 1
    return answer