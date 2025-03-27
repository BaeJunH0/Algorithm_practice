def solution(progresses, speeds):
    answer = []
    count = 0
    length = len(speeds)
    while count < length:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
            
        temp = 0
        while count < length and progresses[count] >= 100:
            count += 1
            temp += 1
        if temp != 0:
            answer.append(temp)
    return answer