import sys

input = sys.stdin.readline

N = 9

def row_check(row, num):
    for i in range(N):
        if num == sdoku[row][i]:
            return False
    return True

def col_check(col, num):
    for i in range(N):
        if num == sdoku[i][col]:
            return False
    return True

def block_check(row, col, num):
    r_start = 3 * (row // 3)
    c_start = 3 * (col // 3)

    for i in range(r_start, r_start + 3):
        for j in range(c_start, c_start + 3):
            if num == sdoku[i][j]:
                return False
    return True

def dfs(depth):
    if depth >= len(zero):
        for ele in sdoku:
            print(''.join(map(str, ele)))
        exit()
    
    row, col = zero[depth]
    for i in range(1, N + 1):
        if row_check(row, i) and col_check(col, i) and block_check(row, col, i):
            sdoku[row][col] = i
            dfs(depth + 1)
            sdoku[row][col] = 0

sdoku = []
zero = []

for i in range(N):
    line = list(map(int, input().rstrip()))

    for j in range(N):
        if line[j] == 0:
            zero.append((i, j))
            
    sdoku.append(line)

dfs(0)