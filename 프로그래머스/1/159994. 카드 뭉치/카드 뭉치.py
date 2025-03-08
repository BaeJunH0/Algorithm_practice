def solution(cards1, cards2, goal):
    index1 = 0
    index2 = 0
    
    for i in goal:
        if len(cards1) > index1 and cards1[index1] == i:
            index1 += 1
        elif len(cards2) > index2 and cards2[index2] == i:
            index2 += 1
        else:
            return 'No'
    return 'Yes'