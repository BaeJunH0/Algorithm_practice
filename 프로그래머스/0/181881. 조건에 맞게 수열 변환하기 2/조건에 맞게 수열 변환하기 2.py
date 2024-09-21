def solution(arr):
    answer = 0
    while True:
        count = 0
        temp = arr[:]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        for i in range(len(arr)):
            if temp[i] == arr[i]:
                count += 1
        if count == len(arr):
            return answer
        answer += 1