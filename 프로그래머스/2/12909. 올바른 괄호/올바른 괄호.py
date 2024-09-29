def solution(s):
    arr = []
    for i in s:
        if i == ')' and len(arr) != 0 and arr[-1] == '(':
            arr.pop()
        else:
            arr.append(i)
    return len(arr) == 0