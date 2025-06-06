# 16 // 2 = 8 ... 0
# 8  // 2 = 4 ... 0
# 4  // 2 = 2 ... 0
# 2  // 2 = 1 ... 0

# 161 // 8 = 20 ... 1
# 20  // 8 = 2  ... 4

def make_line(n, seq):
    line = ''
    count = 0
    while len(line) < seq:
        line += make_n_number(count, n)
        count += 1
    
    return line

def make_n_number(number, n):
    if number == 0:
        return '0'
    temp = []
    while number // n > 0:
        temp.append(number%n)
        number //= n
    temp.append(number)
    
    response = ''
    for i in temp[::-1]:
        if i == 10:
            response += 'A'
        elif i == 11:
            response += 'B'
        elif i == 12:
            response += 'C'
        elif i == 13:
            response += 'D'
        elif i == 14:
            response += 'E'
        elif i == 15:
            response += 'F'
        else:
            response += str(i)
    return response
    
def solution(n, t, m, p):
    answer = ''
    string = make_line(n, t*m)
    for i in range(p-1, t*m, m):
        answer += string[i]
    return answer