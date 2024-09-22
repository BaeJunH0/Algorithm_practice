def solution(s):
    numbers = []
    temp = s.split(' ')
    for i in temp:
        numbers.append(int(i))
    answer = str(min(numbers)) + " " +  str(max(numbers))
    return answer