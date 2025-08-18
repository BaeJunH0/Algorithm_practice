import sys

input = sys.stdin.readline

length, target_x, target_y = map(int, input().rstrip().split())

def search(x, y, size, count):
    global target_x
    global target_y

    temp = [[0, 0], [0, 1], [1, 0], [1, 1]]

    if size == 1:
        for i in range(4):
            if x + temp[i][0] == target_x and y + temp[i][1] == target_y:
                return count + i
    else:
        for i in range(4):
            next_x = x + temp[i][0] * (2 ** (size-1))
            next_y = y + temp[i][1] * (2 ** (size-1))
            next_size = size - 1
            next_count = count + i * 4 ** (next_size)

            if next_x <= target_x < next_x + 2 ** next_size:
                if next_y <= target_y < next_y + 2 ** next_size:
                    return search(next_x, next_y, next_size, next_count)

print(search(0, 0, length, 0))