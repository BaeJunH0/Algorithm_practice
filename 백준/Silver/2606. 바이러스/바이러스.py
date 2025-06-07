import sys
from collections import deque
input = sys.stdin.readline

computer = int(input())
network = int(input())

networks = [[] for i in range(computer + 1)]
visited = [0 for i in range(computer + 1)]

for i in range(network):
    a, b = map(int, input().rstrip().split())
    networks[a].append(b)
    networks[b].append(a)

visited[1] = 1
queue = deque([1])

while len(queue) > 0:
    target = queue.popleft()
    for i in networks[target]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1

answer = 0
for i in range(2, computer+1):
    if visited[i] == 1:
        answer += 1
print(answer)  