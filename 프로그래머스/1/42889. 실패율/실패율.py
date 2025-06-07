def solution(N, stages):
    arr = []
    for i in range(1, N+1):
        dodal = 0
        silpae = 0
        for j in stages:
            if j > i:
                dodal += 1
            if j == i:
                dodal += 1
                silpae += 1
                
        if dodal == 0:
            dodal = 1
            silpae = 0
        arr.append([i, dodal, silpae])
    arr.sort(key=lambda x : (x[2] / x[1], -x[0]), reverse = True)
    
    answer = [x[0] for x in arr]
    return answer