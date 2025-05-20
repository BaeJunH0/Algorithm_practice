def solution(topping):
    answer = 0
    
    temp1 = []
    count = set()
    for i in topping:
        count.add(i)
        temp1.append(len(count))
    
    topping = topping[::-1]
    temp2 = []
    count = set()
    for i in topping:
        count.add(i)
        temp2.append(len(count))
        
    temp2 = temp2[::-1]
    
    for i in range(len(temp1) - 1):
        if temp1[i] == temp2[i+1]:
            answer += 1
    
    return answer