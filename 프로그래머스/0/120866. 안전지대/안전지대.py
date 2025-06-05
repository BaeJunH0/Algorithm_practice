def findBomb(board, x, y):
    danger = [[0, 1], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [1, 0], [1, 1]]
    
    if board[x][y] != 1:
        return board
    
    for i in danger:
        tx = x + i[0]
        ty = y + i[1]
        if tx < len(board) and tx >= 0 and ty < len(board) and ty >= 0:
            if board[tx][ty] != 1:
                board[tx][ty] = 2
    return board

def solution(board):
    length = len(board)
    
    for i in range(length):
        for j in range(length):
            board = findBomb(board, i, j)
    
    answer = 0
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
    return answer