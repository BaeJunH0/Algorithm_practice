def solution(a, b):
    answer = ''
    sumn = 0
    d = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, a-1):
        sumn += day[i]
    sumn += b
    
    return d[sumn % 7 - 1]