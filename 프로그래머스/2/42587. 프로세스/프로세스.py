def solution(priorities, location):
    answer = 0
    if len(priorities) == 1:
        return 1
    
    while True:
        # dequeue
        target = priorities[0]
        priorities = priorities[1:]
        
        # 프로세스 실행 판정
        if len(priorities) == 0:
            answer += 1
            break
        if target >= max(priorities):
            answer += 1
            # 실행한 프로세스 = location에 해당하면 종료
            if location == 0:
                break
        else:
            priorities.append(target)
        
        # Location 조정
        if location == 0:
            location = len(priorities) - 1
        else:
            location -= 1
            
    return answer