def solution(s):
    answer = []
    s = s[1:len(s)-1]
    
    arr = []
    temp = []
    temp_n = ''
    for i in s:
        if i == '{':
            continue
        elif i == '}':
            if len(temp_n) != 0:
                temp.append(int(temp_n))
            arr.append(temp)
            temp = []
            temp_n = ''
        elif i == ',':
            if len(temp_n) != 0:
                temp.append(int(temp_n))
                temp_n = ''
        else:
            temp_n += i
    arr.sort(key = lambda x : len(x))
    
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer