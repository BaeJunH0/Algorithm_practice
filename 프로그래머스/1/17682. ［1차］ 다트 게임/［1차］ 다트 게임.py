def solution(dartResult):
    score = []
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '0' and i != 0 and dartResult[i-1].isdigit():
                score[-1] = int(str(score[-1]) + '0')
            else:
                score.append(int(dartResult[i]))
        else:
            if dartResult[i] == 'S':
                continue
            elif dartResult[i] == 'D':
                score[-1] = score[-1] ** 2
            elif dartResult[i] == 'T':
                score[-1] = score[-1] ** 3
            elif dartResult[i] == '*':
                score[-1] *= 2
                if len(score) > 1:
                    score[-2] *= 2
            elif dartResult[i] == '#':
                score[-1] *= -1
                    
    return sum(score)