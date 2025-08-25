def solution(lottos, win_nums):
    answer = []
    num_zero = 0
    num_correct = 0
    
    sorted_lottos = sorted(lottos)
    
    for i in sorted_lottos:
        if i == 0:
            num_zero += 1
        else:
            if i in win_nums:
                num_correct += 1
    
    prize = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    
    answer.append(prize[num_correct + num_zero])
    answer.append(prize[num_correct])
    
    return answer