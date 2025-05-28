import sys
sys.setrecursionlimit(1000000)

answer = 0
def find(numbers, target, seq):
    if len(numbers) - 1 < seq:
        global answer
        if sum(numbers) == target:
            answer += 1
        return
    
    find(numbers, target, seq + 1)
    
    numbers[seq] *= -1
    find(numbers, target, seq + 1)
    
def solution(numbers, target):
    global answer
    find(numbers, target, 0)
    
    return answer