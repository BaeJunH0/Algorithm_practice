def solution(arr):
    if len(arr) == 1:
        return [-1]
    minn = 99999999
    for i in arr:
        if minn > i:
            minn = i
    arr.pop(arr.index(minn))
    return arr