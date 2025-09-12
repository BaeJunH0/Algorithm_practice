import sys

input = sys.stdin.readline

# 부모 찾기
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

# 부모 합치기
def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 정점 개수
seq = int(input())

# 정점의 부모 (제일 처음 거로 재귀적 갱신)
parents = [i for i in range(seq)]

# 인접행렬로 그래프 표현
graph = [list(map(int, input().rstrip().split())) for _ in range(seq)]

# edge 정보로 그래프 표현
edges = []

# edge 정보 저장
for i in range(seq):
    for j in range(i + 1, seq):
        edges.append((graph[i][j], i, j))

# 가중치 작은 순으로 정렬
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)