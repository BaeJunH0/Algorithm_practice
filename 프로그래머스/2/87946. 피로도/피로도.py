from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):
        current_k = k
        count = 0
        
        for j in i:
            if j[0] > current_k:
                break
            current_k -= j[1]
            count += 1  
        if answer < count:
            answer = count
            
    return answer