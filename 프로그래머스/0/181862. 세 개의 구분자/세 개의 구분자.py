def solution(myStr):
    answer = []
    temp = ''
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            if temp != '':
                answer.append(temp)
                temp = ''     
        else:
            temp += i
    if temp != '':
        answer.append(temp)
    if len(answer) == 0:
        return ["EMPTY"]
    return answer