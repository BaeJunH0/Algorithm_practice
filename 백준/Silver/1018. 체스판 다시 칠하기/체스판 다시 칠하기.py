# 체스판 다시 칠하기
import sys
input = sys.stdin.readline

def test(s1):
    sumi = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] != s1[i][j]:
                sumi += 1
    if sumi < 32:
        return sumi
    else:
        return 64 - sumi

row, col = map(int, input().split())
arr = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 
'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

buffer = []
for i in range(row):
    buffer.append([])
    buffer[i] = list(input().strip())

arri = []
for i in range(row - 7):
    for j in range(col - 7):
        temp = []
        for k in range(8):
            temp.append(buffer[i + k][0 + j:8 + j])
        arri.append(test(temp))
if row == col == 8:
    arri.append(test(buffer))

print(min(arri))