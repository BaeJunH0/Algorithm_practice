def solve(string, index):
    if len(string) < 2:
        return False
    possible = ["aya", "ye", "woo", "ma"]
    
    last = ''
    while True:
        if index == len(string):
            return True
        elif index > len(string):
            return False
        elif string[index:index+2] in possible and string[index:index+2] != last:
            last = string[index:index+2]
            index += 2
        elif string[index:index+3] in possible and string[index:index+3] != last:
            last = string[index:index+3]
            index += 3
        else:
            return False

def solution(babbling):
    answer = 0
    for i in babbling:
        answer += solve(i, 0)
    return answer