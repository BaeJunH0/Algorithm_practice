def solution(skill, skill_trees):
    answer = 0
    
    for case in skill_trees:
        status = True
        
        now_useableable = 0
        for one in case:
            if one in skill:
                if skill.index(one) == now_useableable:
                    now_useableable += 1
                else:
                    status = False
                    break   
        if status:
            answer += 1
                
    return answer