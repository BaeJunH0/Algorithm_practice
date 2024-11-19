def solution(food):
    answer = ''
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            answer += str(i)
    temp = answer[::-1]
    answer += '0'
    answer += temp
    return answer