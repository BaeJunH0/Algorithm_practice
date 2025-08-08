def solution(phone_book):
    dic = {}
    for i in phone_book:
        dic[i] = 1
    
    for i in phone_book:
        temp = ''
        for j in i[:-1]:
            temp += j
            if temp in dic.keys():
                return False
    return True