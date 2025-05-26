from itertools import combinations
def solution(nums):
    answer = 0
    # 나올 수 있는 합의 최대 값
    pnum = 3000
    # 소수 판별 리스트
    era = [0, 0] + [1] * (pnum - 1)    
    for i in range(2, pnum + 1):
        if era[i] == 1:
            for j in range(i * 2, pnum + 1, i):
                era[j] = 0
    
    comb = combinations(nums, 3)
    for i in comb:
        if era[sum(i)] == 1:
            answer += 1

    return answer