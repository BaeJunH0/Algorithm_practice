def solution(arr):
    ind = []
    for i in range(len(arr)):
        if arr[i] == 2:
            ind.append(i)
    if len(ind) == 0:
        return [-1]
    if len(ind) == 1:
        return [2]
    answer = arr[ind[0]:ind[-1]+1]
    return answer