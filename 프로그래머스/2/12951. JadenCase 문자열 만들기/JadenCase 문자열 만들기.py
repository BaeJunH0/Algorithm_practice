def solution(s):
    answer = ''
    temp = s.split(' ')
    for i in temp:
        answer += i[:1].upper() + i[1:].lower() + " "
    answer = answer[:-1]
    return answer