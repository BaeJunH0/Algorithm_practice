def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for i in s:
        if ord(i) < 48 or ord(i) > 58:
            return False
    return True