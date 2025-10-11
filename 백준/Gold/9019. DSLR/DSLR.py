import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
    queue = deque([a])
    visited = [False] * 10000
    visited[a] = True

    # 경로 기록용 배열
    from_command = [''] * 10000
    from_where = [-1] * 10000

    while queue:
        cur = queue.popleft()

        if cur == b:
            # 역추적
            result = []
            while cur != a:
                result.append(from_command[cur])
                cur = from_where[cur]
            return ''.join(reversed(result))

        # D
        nxt = (cur * 2) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            from_command[nxt] = 'D'
            from_where[nxt] = cur
            queue.append(nxt)

        # S
        nxt = (cur - 1) % 10000  # (cur == 0이면 9999)
        if not visited[nxt]:
            visited[nxt] = True
            from_command[nxt] = 'S'
            from_where[nxt] = cur
            queue.append(nxt)

        # L
        nxt = (cur % 1000) * 10 + cur // 1000
        if not visited[nxt]:
            visited[nxt] = True
            from_command[nxt] = 'L'
            from_where[nxt] = cur
            queue.append(nxt)

        # R
        nxt = (cur // 10) + (cur % 10) * 1000
        if not visited[nxt]:
            visited[nxt] = True
            from_command[nxt] = 'R'
            from_where[nxt] = cur
            queue.append(nxt)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a, b))
