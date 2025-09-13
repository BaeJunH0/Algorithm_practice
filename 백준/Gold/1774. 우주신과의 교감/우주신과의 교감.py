import sys

input = sys.stdin.readline

def edge_length(a : tuple, b : tuple) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])

    return parents[x]

def union_parents(a, b):
    x, y = find_parents(a), find_parents(b)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

N, M = map(int, input().rstrip().split())
node = [()]
linked_edges = []
edges = []
parents = [i for i in range(N + 1)]

# 노드
for i in range(N):
    node.append(tuple(map(int, input().rstrip().split())))

# 이미 연결된 엣지
for i in range(M):
    a, b = map(int, input().rstrip().split())

    union_parents(a, b)

# 노드들의 연결 표시
for i in range(1, N + 1):
    for j in range(i+1, N + 1):
        edges.append((edge_length(node[i], node[j]), i, j))

edges.sort()

result = 0
for edge in edges:
    weight, a, b = edge
    if find_parents(a) != find_parents(b):
        union_parents(a, b)
        result += weight

print(f'{result:.2f}')