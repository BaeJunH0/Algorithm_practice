import copy

def isAlphabet(string):
    answer = False
    if 65 <= ord(string) and 90 >= ord(string):
        answer = True
    if 97 <= ord(string) and 122 >= ord(string):
        answer = True
    return answer

def solution(str1, str2):
    dic1 = {}
    dic2 = {}
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    for i in range(len(str1) - 1):
        if isAlphabet(str1[i]) and isAlphabet(str1[i+1]):
            ele = str1[i] + str1[i+1]
            if ele not in dic1.keys():
                dic1[ele] = 1
            else:
                dic1[ele] += 1
        
    for i in range(len(str2) - 1):
        if isAlphabet(str2[i]) and isAlphabet(str2[i+1]):
            ele = str2[i] + str2[i+1]
            if ele not in dic2.keys():
                dic2[ele] = 1
            else:
                dic2[ele] += 1
            
    temp1 = copy.deepcopy(dic1)
    temp2 = copy.deepcopy(dic2)
    
    son = 0
    for i in temp1.keys():
        for j in range(temp1[i]):
            if i in temp2.keys() and temp2[i] != 0:
                son += 1
                temp2[i] -= 1
    
    mother = 0
    for i in dic1.keys():
        if i not in dic2.keys():
            mother += dic1[i]
        else:
            mother += max(dic1[i], dic2[i])
    for i in dic2.keys():
        if i not in dic1.keys():
            mother += dic2[i]
    
    if mother == 0:
        return 65536

    return int((son / mother) * 65536)