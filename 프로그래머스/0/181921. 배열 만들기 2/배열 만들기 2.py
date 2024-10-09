from itertools import permutations
def solution(l, r):
    length = len(str(r))
    temp = '0' * length + '5' * length
    answer = list(set(permutations(temp, length)))
    real = []
    for i in answer:
        k = ''
        for j in range(length):
            k += i[j]
        if int(k) >= l and int(k) <= r:
            real.append(int(k))
    real.sort()
    if len(real) == 0:
        return [-1]
    return real