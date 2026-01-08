from collections import deque

def solution(numbers, target):
    answer = 0
    arr = [numbers[0], -numbers[0]]
    
    for i in range(1, len(numbers)):
        temp = []
        for value in arr:
            temp.append(value + numbers[i])
            temp.append(value - numbers[i])
        arr = temp
    
    for i in arr:
        if i == target:
            answer += 1
    
    return answer