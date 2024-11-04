def solution(s):
    answer = ''
    ind = 0
    while ind < len(s):
        if s[ind] == 'o':
            answer += '1'
            ind += 3
        elif s[ind] == 'z':
            answer += '0'
            ind += 4
        elif s[ind] == 't':
            if s[ind + 1] == 'w':
                answer += '2'
                ind += 3
            else:
                answer += '3'
                ind += 5
        elif s[ind] == 'f':
            if s[ind + 1] == 'o':
                answer += '4'
            else:
                answer += '5'
            ind += 4
        elif s[ind] == 's':
            if s[ind + 1] == 'i':
                answer += '6'
                ind += 3
            else:
                answer +='7'
                ind += 5
        elif s[ind] == 'e':
            answer += '8'
            ind += 5
        elif s[ind] == 'n':
            answer += '9'
            ind += 4
        else:
            answer += s[ind]
            ind += 1
    answer = int(answer)
    return answer