def solution(rank, attendance):
    temp = []
    length = len(rank)
    dic = {}
    check = {}
    
    for i in range(length):
        dic[rank[i]] = attendance[i]
        check[rank[i]] = i

    for i in range(1, length + 1):
        if dic[i]:
            temp.append(check[i])
        if len(temp) == 3:
            break
            
    return 10000 * temp[0] + 100 * temp[1] + 1 * temp[2]