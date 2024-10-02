def solution(my_string, overwrite_string, s):
    answer = ''
    length = len(overwrite_string)
    answer += my_string[:s]
    answer += overwrite_string
    answer += my_string[s+length:]
    return answer