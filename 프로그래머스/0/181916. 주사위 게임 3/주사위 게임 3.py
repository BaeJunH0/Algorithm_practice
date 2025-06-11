def solution(a, b, c, d):
    answer = 0
    arr = list([a, b, c, d])
    arr.sort()
    if a == b == c == d:
        return a * 1111
    elif arr[0] == arr[1] == arr[2]:
        return (arr[0] * 10 + arr[3]) ** 2
    elif arr[1] == arr[2] == arr[3]:
        return (arr[3] * 10 + arr[0]) ** 2
    elif arr[0] == arr[1] and arr[2] == arr[3]:
        tmp = arr[0] + arr[3]
        temp = arr[0] - arr[3] if arr[0] - arr[3] > 0 else arr[3] - arr[0]  
        return tmp * temp
    elif arr[0] == arr[1] and arr[2] != arr[3]:
        return arr[2] * arr[3]
    elif arr[1] == arr[2]:
        return arr[0] * arr[3]
    elif arr[0] != arr[1] and arr[2] == arr[3]:
        return arr[0] * arr[1]
    else:
        return arr[0]