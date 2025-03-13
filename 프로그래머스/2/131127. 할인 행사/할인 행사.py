def isSame(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
def solution(want, number, discount):
    answer = 0
    snum = len(discount) - sum(number)
    temp = []
    for i in range(len(want)):
        for j in range(number[i]):
            temp.append(want[i])
    temp.sort()
    
    for i in range(0, snum+1):
        arr = discount[i:i+10]
        arr.sort()
        if isSame(arr, temp):
            answer += 1
        
    return answer