def solution(elements):
    temp = []
    length = len(elements)
    
    # 길이 값 i
    for i in range(1, length + 1):
        # 시작 지점 j
        for j in range(length):
            sumn = 0
            # j부터 i만큼 탐색
            if j + i > length:
                sumn += sum(elements[j:length]) + sum(elements[0:i-(length-j)])
            else:
                sumn += sum(elements[j:j+i])
            temp.append(sumn)
    
    temp = list(set(temp))
            
    return len(temp)