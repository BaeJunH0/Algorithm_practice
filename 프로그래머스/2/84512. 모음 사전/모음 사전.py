from itertools import product
def solution(word):
    target = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1, 6):
        arr += list(map(''.join, product(target, repeat = i)))
    arr.sort()
    answer = arr.index(word) + 1
    return answer