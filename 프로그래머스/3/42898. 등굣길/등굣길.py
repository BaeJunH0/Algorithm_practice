def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 시작점은 1
            if i == 1 and j == 1: continue
            
            # 물웅덩이 일 때 0으로 초기화 (지나는 경우의 수 없음)
            if [i,j] in puddles:
                dp[i][j] = 0
            else:                
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            
    return dp[n][m]