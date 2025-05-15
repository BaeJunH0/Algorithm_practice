def solution(answers):
    answer = []
    man_answer = [0, 0, 0]
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == man1[i % 5]:
            man_answer[0] += 1
        if answers[i] == man2[i % 8]:
            man_answer[1] += 1
        if answers[i] == man3[i % 10]:
            man_answer[2] += 1
            
    max_num = max(man_answer)
    for i in range(len(man_answer)):
        if man_answer[i] == max_num:
            answer.append(i + 1)
            
    return answer