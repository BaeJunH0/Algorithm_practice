def solution(n, words):
    log = []
    temp = ''
    for i in range(len(words)):
        if len(temp) == 0:
            log.append(words[i])
            temp = words[i]
            continue
        if temp[-1] != words[i][0]:
            return [i % n + 1, i // n + 1]
        elif words[i] in log:
            return [i % n + 1, i // n + 1]
        else:
            log.append(words[i])
            temp = words[i]
    return [0, 0]