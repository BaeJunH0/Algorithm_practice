import sys

w_sum = 0
b_sum = 0

# 재귀 분할 정복
def solve(x1, y1, x2, y2, table):
    global w_sum
    global b_sum

    now = x2 - x1 + 1

    # 재귀 호출
    # 8 -> 4 -> 2 -> 1
    if now == 1:
        if table[x1][y1] == 0:
            w_sum += 1
        else:
            b_sum += 1
        return
    
    state = 1
    for i in range(x1, x2 + 1):
        if state == 0:
            break
        for j in range(y1, y2 + 1):
            if table[i][j] != table[x1][y1]:
                state = 0
                break
    
    if state == 0:
        solve(x1, y1, x1 + now // 2 - 1, y1 + now // 2 - 1, table)
        solve(x1 + now // 2, y1, x2, y1 + now // 2 - 1, table)
        solve(x1, y1 + now // 2, x1 + now // 2 - 1, y2, table)
        solve(x1 + now // 2, y1 + now // 2, x2, y2, table)

    else:
        if table[x1][y1] == 0:
            w_sum += 1
        else:
            b_sum += 1
    

input = sys.stdin.readline

seq = int(input())

table = []

# 입력 받기
for i in range(seq):
    temp = list(map(int, input().rstrip().split()))
    table.append(temp)

# 검증 하기
solve(0, 0, seq-1, seq-1, table)

print(w_sum)
print(b_sum)