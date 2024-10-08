def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer += chr(ord('A') + (ord(i) - ord('A') + n) % 26)
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            answer += chr(ord('a') + (ord(i) - ord('a') + n) % 26)
        else:
            answer += i
    return answer