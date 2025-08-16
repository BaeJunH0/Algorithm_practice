import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, k):
    MAX = 10 ** 5
    line = [0 for i in range(MAX + 1)]

    queue = deque()
    queue.append([n, 0])

    while queue:
        now, count = queue.popleft()
        line[now] = 1

        if now == k:
            return count
        
        for i in [now -1, now + 1, now * 2]:
            if 0 <= i <= MAX and line[i] == 0:
                queue.append([i, count + 1])

    return -1

n, k = map(int, input().rstrip().split())

print(bfs(n, k))


