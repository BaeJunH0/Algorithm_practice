import sys
input = sys.stdin.readline
INF = sys.maxsize

def warmhole():
    distance = [INF] * (v + 1)
    distance[1] = 0

    for i in range(v):
        for cur, nxt, cost in graph:
            if distance[nxt] > distance[cur] + cost:
                distance[nxt] = distance[cur] + cost

                if i == v - 1:
                    return True
    return False

T = int(input())
for _ in range(T):
    v, e, hole = map(int, input().split())
    graph = []

    # 일반 간선
    for _ in range(e):
        a, b, w = map(int, input().split())
        graph.append((a, b, w))
        graph.append((b, a, w))

    # 웜홀
    for _ in range(hole):
        a, b, w = map(int, input().split())
        graph.append((a, b, -w))

    has_cycle = warmhole()

    print("YES" if has_cycle else "NO")
