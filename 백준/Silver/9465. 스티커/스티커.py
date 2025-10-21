import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    seq = int(input())
    arr = []

    arr.append(list(map(int, input().rstrip().split())))
    arr.append(list(map(int, input().rstrip().split())))

    if seq == 1:
        print(max(arr[0][0], arr[1][0]))
        continue

    arr[1][1] += arr[0][0]
    arr[0][1] += arr[1][0]

    for i in range(2, seq):
        arr[0][i] = arr[0][i] + max(arr[1][i-1], arr[0][i-2], arr[1][i-2])
        arr[1][i] = arr[1][i] + max(arr[0][i-1], arr[0][i-2], arr[1][i-2])

    print(max(arr[0][-1], arr[1][-1]))