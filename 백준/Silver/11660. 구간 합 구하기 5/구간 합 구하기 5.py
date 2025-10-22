import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    temp = list(map(int, input().rstrip().split()))
    for j in range(0, N):
        arr[i][j + 1] = arr[i][j] + temp[j] + (arr[i-1][j+1] - arr[i-1][j])
    

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())

    response = arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]
    print(response)