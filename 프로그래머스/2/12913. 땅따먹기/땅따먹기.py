def solution(land):
    dp = [[x for x in land[0]]] + [[0] * 4 for _ in range(len(land) - 1)]
    
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][:j] + dp[i-1][j+1:]) + land[i][j]
    
    return max(dp[-1])