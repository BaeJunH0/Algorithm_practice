def solution(s):
    temp = len(s)
    if temp % 2 == 0:
        return s[temp//2-1] + s[temp//2]
    else:
        return s[temp//2]