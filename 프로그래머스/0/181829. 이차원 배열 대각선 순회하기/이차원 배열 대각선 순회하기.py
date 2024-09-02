def solution(board, k):
    answer = 0
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if i + j <= k:
                answer += board[i][j]
    return answer