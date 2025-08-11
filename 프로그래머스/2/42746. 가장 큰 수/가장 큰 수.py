def solution(numbers):
    answer = ''
    sorted_num = sorted(numbers, key = lambda x : str(x) * 3, reverse = True)
    
    for i in sorted_num:
        if i == 0 and (answer == '' or answer == '0'):
            continue
        answer += str(i)
        
    return '0' if answer == '' else answer