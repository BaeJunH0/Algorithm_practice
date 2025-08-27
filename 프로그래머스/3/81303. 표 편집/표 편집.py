def solution(n, k, cmd):
    # pyp[n]의 0번째 원소 : 인덱스, 1번째 원소 : 현재 이전 인덱스, 2번째 원소 : 현재 다음 인덱스
    pyo = [[x, x - 1, x + 1] for x in range(n)]
    pyo[-1][-1] = -1
    answer = ['O'] * n
    
    cache, now = [], k
    
    for i in cmd:
        command = i.split()
        if command[0] == 'U':
            for _ in range(int(command[1])):
                now = pyo[now][1]
        elif command[0] == 'D':
            for _ in range(int(command[1])):
                now = pyo[now][2]
        elif command[0] == 'C':
            cache.append(now)
            answer[now] = 'X'
            
            # 마지막 원소일 때
            if pyo[now][2] == -1:
                now = pyo[now][1]
                pyo[now][2] = -1
            # 첫 번째 원소일 때
            elif pyo[now][1] == -1:
                now = pyo[now][2]
                pyo[now][1] = -1
            # 이외
            else:
                pyo[pyo[now][1]][2] = pyo[now][2]
                pyo[pyo[now][2]][1] = pyo[now][1]
                now = pyo[now][2]
        elif command[0] == 'Z':
            target = cache.pop()
            answer[target] = 'O'
            
            # 복구한 놈이 첫 번째 일 때
            if pyo[pyo[target][2]][1] == -1:
                pyo[pyo[target][2]][1] = target
            # 복구한 놈이 마지막일 때
            elif pyo[pyo[target][1]][2] == -1:
                pyo[pyo[target][1]][2] = target
            # 이외
            else:
                pyo[pyo[target][2]][1] = target
                pyo[pyo[target][1]][2] = target
                
    return ''.join(answer)