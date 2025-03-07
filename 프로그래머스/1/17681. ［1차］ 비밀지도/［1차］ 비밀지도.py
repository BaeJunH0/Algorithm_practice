def decimalToBin(n, num):
    binNum = ''
    while num // 2 != 0:
        binNum += str(num % 2)
        num //= 2
    if num == 1:
        binNum += '1'
    
    binNum = binNum[::-1]
    while len(binNum) < n:
        binNum = '0' + binNum
    return binNum

def solution(n, arr1, arr2):
    map1 = []
    for i in range(len(arr1)):
        temp = ''
        for j in decimalToBin(n, arr1[i]):
            if j == '1':
                temp += '#'
            else:
                temp += ' '
        map1.append(temp)
        
    map2 = []
    for i in range(len(arr2)):
        temp = ''
        for j in decimalToBin(n, arr2[i]):
            if j == '1':
                temp += '#'
            else:
                temp += ' '
        map2.append(temp)
    
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if map1[i][j] == ' ' and map2[i][j] == ' ':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
        
    return answer