def solution(N, road, K):
    INF = 9999999
    
    arr = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        arr[i][i] = 0
        
    for a, b, length in road:
        if arr[a][b] > length:
            arr[a][b] = length
            arr[b][a] = length

    visited = [1] + [0] * (N)
    
    for _ in range(N):
        target = INF
        index = -1
        # 이번에 거칠 정점 선정
        for i in range(1, N + 1):
            if arr[1][i] < target and visited[i] == 0:
                target = arr[1][i]
                index = i
        # 1 -> 정점 -> i 일때 더 효율적인지 확인
        for i in range(1, N + 1):
            if arr[1][i] > arr[1][index] + arr[index][i]:
                arr[1][i] = arr[1][index] + arr[index][i]
                
        visited[index] = 1
    
    answer = 0
    for i in arr[1]:
        if i <= K:
            answer += 1
            
    return answer