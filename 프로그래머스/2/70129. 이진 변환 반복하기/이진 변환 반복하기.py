def checkZero(s):
    count = 0
    for i in s:
        if i == '0':
            count += 1
    return count

def solution(s):
    count = 0
    zero = 0
    
    while s != '1':
        delete = checkZero(s)
        zero += delete
        s = bin(len(s)-delete)[2:]
        count += 1
    return [count, zero]