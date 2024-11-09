def solution(a, b, n):
    answer = 0
    coke = n
    while True:
        answer += coke // a * b
        coke = coke // a * b + coke % a
        if coke // a < 1:
            break
    return answer