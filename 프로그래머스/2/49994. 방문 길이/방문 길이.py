def solution(dirs):
    # U, D, R, L
    map_arr = [[[0 for _ in range(4)] for i in range(11)] for j in range(11)]
    answer = 0
    x, y = 5, 5
    for i in dirs:
        if i == 'U':
            if y + 1 > 10:
                continue
            if map_arr[x][y][0] == 0 and map_arr[x][y+1][1] == 0:
                map_arr[x][y][0] = map_arr[x][y+1][1] = 1
                answer += 1
            y += 1
        elif i == 'D':
            if y - 1 < 0:
                continue
            if map_arr[x][y][1] == 0 and map_arr[x][y-1][0] == 0:
                map_arr[x][y][1] = map_arr[x][y-1][0] = 1
                answer += 1
            y -= 1
        elif i == 'R':
            if x + 1 > 10:
                continue
            if map_arr[x][y][2] == 0 and map_arr[x+1][y][3] == 0:
                map_arr[x][y][2] = map_arr[x+1][y][3] = 1
                answer += 1
            x += 1
        else:
            if x - 1 < 0:
                continue
            if map_arr[x][y][3] == 0 and map_arr[x-1][y][2] == 0:
                map_arr[x][y][3] = map_arr[x-1][y][2] = 1
                answer += 1
            x -= 1
    return answer