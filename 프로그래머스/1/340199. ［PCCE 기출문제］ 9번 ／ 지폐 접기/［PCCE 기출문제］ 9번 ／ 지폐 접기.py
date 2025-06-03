def solution(wallet, bill):
    answer = 0
    small = wallet[0] if wallet[0] < wallet[1] else wallet[1]
    big = wallet[0] if wallet[0] >= wallet[1] else wallet[1]
    
    while True:
        if min(bill) <= small and max(bill) <= big:
            return answer
        
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        