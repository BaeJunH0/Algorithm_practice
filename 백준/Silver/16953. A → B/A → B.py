import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

queue = deque()
queue.append((a, 1))

while queue:
    target, count = queue.popleft()

    if target == b:
        print(count)
        exit()

    if target * 2 <= b:
        queue.append((target * 2, count + 1))

    if int(str(target) + '1') <= b:
        queue.append((int(str(target) + '1'), count + 1))

print(-1)