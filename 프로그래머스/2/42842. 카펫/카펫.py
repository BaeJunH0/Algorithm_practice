def solution(brown, yellow):
    row = []
    col = []
    every = brown + yellow
    for i in range(3, int(every**0.5) + 1):
        if every % i == 0:
            row.append(i)
            col.append(every // i)
    for i in range(len(row)):
        if (row[i] - 2) * (col[i] - 2) == yellow:
            return [col[i], row[i]]