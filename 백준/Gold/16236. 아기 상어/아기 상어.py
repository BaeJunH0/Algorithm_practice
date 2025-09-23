import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input())

shark = []
field = []

for i in range(N):
    line = list(map(int, input().rstrip().split()))
    temp = []

    for j in range(N):
        if line[j] == 9:
            shark = [i, j]
            temp.append(0)
        else:
            temp.append(line[j])
    field.append(temp)

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
count = 0
shark_size = 2
feed = 0

while True:
    queue = deque()
    queue.append(shark)

    check = [[0] * N for _ in range(N)]
    fishes = []

    while queue:
        a, b = queue.popleft()

        for x, y in dir:
            na, nb = a + x, b + y
            if 0 <= na < N and 0 <= nb < N and check[na][nb] == 0:
                if field[na][nb] <= shark_size:
                    queue.append([na, nb])
                    check[na][nb] += check[a][b] + 1

                    if 0 < field[na][nb] < shark_size:
                        fishes.append([check[na][nb], na, nb])

    if not fishes:
        break

    fishes.sort()

    step, row, col = fishes[0]

    count += step
    feed += 1

    if feed == shark_size:
        shark_size += 1
        feed = 0

    field[row][col] = 0
    shark = [row, col]

print(count)