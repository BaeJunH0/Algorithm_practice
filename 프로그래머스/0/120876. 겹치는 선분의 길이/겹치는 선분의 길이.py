def solution(lines):
    answer = 0
    sorted_lines = sorted(lines, key = lambda x : x[1])
    last = sorted_lines[-1][-1] 
    
    sorted_lines = sorted(lines, key = lambda x : x[0])
    first = sorted_lines[0][0]
    
    line = [0] * (last - first + 1)
    
    for a, b in lines:
        for i in range(a, b):
            line[i - first] += 1
    
    for i in line:
        if i > 1:
            answer += 1
    
    return answer