def solution(n, m, section):
    answer = 0
    next = 0
    for i in section:
        if next >= i:
            continue
        next = i + m - 1
        answer += 1
        
    return answer