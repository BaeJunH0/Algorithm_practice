def solution(arr, k):
    temp = []
    for i in arr:
        if i not in temp:
            temp.append(i)
        if len(temp) == k:
            return temp
    for i in range(k - len(temp)):
        temp.append(-1)
    return temp