import sys

input = sys.stdin.readline

s_node, s_edge = map(int, input().rstrip().split())

arr = [[sys.maxsize] * (s_node + 1) for _ in range(s_node + 1)]

for i in range(s_edge):
    a, b = map(int, input().rstrip().split())
    arr[a][b], arr[b][a] = 1, 1

for i in range(1, s_node + 1):
    visited = [0] * (s_node + 1)
    visited[0] = visited[i] = 1
    for _ in range(1, s_node):
        small = sys.maxsize
        idx = -1

        for j in range(1, s_node + 1):
            if visited[j] == 0 and small > arr[i][j]:
                small, idx = arr[i][j], j
        
        for j in range(1, s_node + 1):
            if arr[i][j] > arr[i][idx] + arr[idx][j]:
                arr[i][j] = arr[i][idx] + arr[idx][j]
        
        visited[idx] = 1

answer = [sum(arr[i][1:]) for i in range(1, s_node + 1)]

min_value = sys.maxsize
min_idx = -1
for i in range(s_node):
    if min_value > answer[i]:
        min_value = answer[i]
        min_idx = i

print(min_idx + 1)