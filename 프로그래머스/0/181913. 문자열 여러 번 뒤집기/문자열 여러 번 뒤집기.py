def solution(my_string, queries):
    answer = my_string
    for i in queries:
        temp1 = answer[:i[0]]
        temp2 = answer[i[0]:i[1]+1]
        temp2 = temp2[::-1]
        temp3 = answer[i[1]+1:]
        answer = temp1 + temp2 + temp3
    return answer