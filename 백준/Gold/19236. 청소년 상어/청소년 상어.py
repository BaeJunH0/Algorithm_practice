import sys
import copy

input = sys.stdin.readline

# 초기 데이터 입력
fish = {}
aqua = []
direction = []

for i in range(4):
    line = list(map(int, input().rstrip().split()))
    t1, t2 = [], []
    for j in range(0, 8, 2):
        fish[line[j]] = [i, j // 2]
        t1.append(line[j])
        t2.append(line[j + 1] - 1)
    aqua.append(t1)
    direction.append(t2)

# 8방향
d = [[-1, 0], [-1, -1], [0, -1], [1, -1],
     [1, 0], [1, 1], [0, 1], [-1, 1]]

# swap 함수
def swap(aqua, direction, fish, a, b):
    x1, y1 = a
    x2, y2 = b
    aqua[x1][y1], aqua[x2][y2] = aqua[x2][y2], aqua[x1][y1]
    direction[x1][y1], direction[x2][y2] = direction[x2][y2], direction[x1][y1]
    fish[aqua[x1][y1]], fish[aqua[x2][y2]] = [x1, y1], [x2, y2]

answer = 0

def dfs(aqua, direction, fish, dead, shark, score):
    global answer

    # 1. 물고기 이동
    for i in range(1, 17):
        if i in dead:
            continue
        x, y = fish[i]
        for _ in range(8):
            a, b = d[direction[x][y]]
            nx, ny = x + a, y + b
            if 0 <= nx < 4 and 0 <= ny < 4 and [nx, ny] != shark:
                swap(aqua, direction, fish, [x, y], [nx, ny])
                break
            direction[x][y] = (direction[x][y] + 1) % 8

    # 2. 상어 이동 후보
    x, y = shark
    a, b = d[direction[x][y]]
    targets = []
    nx, ny = x + a, y + b
    while 0 <= nx < 4 and 0 <= ny < 4:
        if aqua[nx][ny] not in dead:
            targets.append([nx, ny])
        nx += a
        ny += b

    # 3. 이동할 곳 없으면 종료
    if not targets:
        answer = max(answer, score)
        return

    # 4. 모든 후보 재귀 탐색
    for tx, ty in targets:
        aqua_copy = copy.deepcopy(aqua)
        direction_copy = copy.deepcopy(direction)
        fish_copy = copy.deepcopy(fish)
        dead_copy = dead[:]

        eaten = aqua_copy[tx][ty]
        dead_copy.append(eaten)
        shark_next = [tx, ty]

        dfs(aqua_copy, direction_copy, fish_copy, dead_copy, shark_next, score + eaten)

# 초기 상어 위치
initial_eaten = aqua[0][0]
dead = [initial_eaten]
shark = [0, 0]

dfs(aqua, direction, fish, dead, shark, initial_eaten)
print(answer)