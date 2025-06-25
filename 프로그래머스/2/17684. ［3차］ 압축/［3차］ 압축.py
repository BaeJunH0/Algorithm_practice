def solution(msg):
    answer = []
    dic = {}
    ind = 1
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = ind
        ind += 1

    number = 0
    while True:
        # 이번 회차 대상 문자
        w = msg[number]
        
        # 종료 조건 : 이번 회차 대상 문자가 마지막 문자인 경우
        if number == len(msg) - 1:
            answer.append(dic[w])
            return answer

        # 다음 문자
        c = msg[number + 1]
        number += 1
        
        while w + c in dic.keys():
            # 종료 조건 : 마지막 문자까지 다 탐색한 경우
            if number == len(msg) - 1:
                answer.append(dic[w+c])
                return answer
            
            w += c
            c = msg[number + 1]
            number += 1
            
        answer.append(dic[w])
        dic[w+c] = ind
        ind += 1
        
        if number == len(msg):
            return answer