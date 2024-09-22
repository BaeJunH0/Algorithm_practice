def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
        else:
            if answer[-1] == arr[i]:
                answer.pop()  
            else:
                answer.append(arr[i])
        i += 1
    if len(answer) == 0:
        return [-1]
    return answer