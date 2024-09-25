def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for i in range(row):
            for j in range(row - col):
                arr[i].append(0)
    if row < col:
        temp = [0] * col
        for i in range(col - row):
            arr.append(temp[:])
    return arr