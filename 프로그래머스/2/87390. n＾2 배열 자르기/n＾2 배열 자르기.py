def solution(n, left, right):
    ls = []
    
    for i in range(left, right + 1):
        col = i // n
        row = i % n

        ls.append(row + 1 if row > col else col + 1)
    return ls