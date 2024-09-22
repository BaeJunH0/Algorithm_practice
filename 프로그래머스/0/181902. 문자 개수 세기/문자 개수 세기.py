def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        if ord(i) >= 65 and ord(i) <= 91:
            answer[ord(i) - 65] += 1
        else:
            answer[ord(i) - 71] += 1
    return answer