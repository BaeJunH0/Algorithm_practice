def solution(order):
    answer = 0
    now = 0
    stack = []
    
    for i in range(1, len(order) + 1):
        if order[now] == i:
            answer += 1
            now += 1
            
            while stack and stack[-1] == order[now]:
                stack.pop()
                now += 1
                answer += 1
        else:
            while stack and stack[-1] == order[now]:
                stack.pop()
                now += 1
                answer += 1
                
            stack.append(i)
    
    return answer