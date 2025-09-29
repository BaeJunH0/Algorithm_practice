import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):
    for a, b in dir:
        nx, ny = x + a, y + b

        if 0 <= nx < h and 0 <= ny < w and not check[nx][ny]:
            if sea[nx][ny] == 1:
                check[nx][ny] = True
                dfs(nx, ny)

while True:
    w, h = map(int, input().rstrip().split())

    if w == h == 0:
        break

    sea = []
    check = [[False] * w for _ in range(h)]
    dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for i in range(h):
        line = list(map(int, input().rstrip().split()))
        sea.append(line)

    count = 0
    for i in range(h):
        for j in range(w):
            if sea[i][j] == 1 and not check[i][j]:
                count += 1
                check[i][j] = True
                dfs(i, j)
    
    print(count)
