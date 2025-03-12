def isCorrect(string):
    if len(string) % 2 != 0:
        return False
    if string == '':
        return True
    
    stack = []
    for i in string:
        if len(stack) == 0:
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == '}' and stack[-1] == '{':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack) == 0:
        return True
    return False

def solution(s):
    answer = 0
    temp = s
    for _ in s:
        if isCorrect(temp):
            answer += 1
        temp = temp[1:] + temp[0]
    return answer