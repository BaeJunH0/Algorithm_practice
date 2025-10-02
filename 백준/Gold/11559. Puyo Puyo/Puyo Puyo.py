import sys
from collections import deque

input = sys.stdin.readline

def boom():
    check = [[False]*col for _ in range(row)]
    popped = False

    for i in range(row):
        for j in range(col):
            if field[i][j] == '.' or check[i][j]:
                continue

            queue = deque([(i, j)])
            check[i][j] = True
            temp = [(i, j)]
            word = field[i][j]

            while queue:
                x, y = queue.popleft()
                for a, b in dir:
                    nx, ny = x+a, y+b
                    if 0 <= nx < row and 0 <= ny < col and not check[nx][ny]:
                        if field[nx][ny] == word:
                            check[nx][ny] = True
                            queue.append((nx, ny))
                            temp.append((nx, ny))

            if len(temp) >= 4:
                popped = True
                for x, y in temp:
                    field[x][y] = '.'

    return popped

        
def relocation():
    for i in range(col):
        temp = []
        for j in range(row):
            if field[j][i] != '.':
                temp.append(field[j][i])
        # 먼저 열 전체를 비운다
        for j in range(row):
            field[j][i] = '.'
        # 바닥부터 채운다
        idx = row - len(temp)
        for t_idx, val in enumerate(temp):
            field[idx + t_idx][i] = val

row, col = 12, 6

field = []
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for i in range(row):
    line = input().rstrip()
    field.append([x for x in line])

cnt = 0
while True:
    if not boom():
        break
    relocation()
    cnt += 1

print(cnt)