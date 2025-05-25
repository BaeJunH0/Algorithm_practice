def solution(n):
    answer = 0
    
    era = [0] * 1000000 + [0]
    
    for i in range(2, int(1000001 ** (0.5))):
        for j in range(i * 2, 1000001, i):
            if j % i == 0:
                era[j] = 1
    for i in range(2, n+1):
        if era[i] == 0:
            answer += 1
    return answer