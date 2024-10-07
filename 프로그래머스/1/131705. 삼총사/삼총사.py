from itertools import combinations

def solution(number):
    answer = 0
    com = combinations(number, 3)
    for i in com:
        if sum(i) == 0:
            answer += 1
    return answer