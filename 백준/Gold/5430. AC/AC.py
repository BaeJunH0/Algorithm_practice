import sys
from collections import deque

input = sys.stdin.readline

seq = int(input())

for _ in range(seq):
    command = input().rstrip()
    temp = int(input())
    queue = deque(input().rstrip()[1:-1].split(','))

    if temp == 0:
        queue = deque()

    flag = 0
    r_count = 0
    for i in command:   
        if i == 'R':
            r_count += 1
        elif i == 'D':
            if queue:
                if r_count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print('error')
                flag = 1
                break
    
    if flag == 1:
        continue

    if r_count % 2 == 0:
        print('[' + ','.join(queue) + ']')
    else:
        queue.reverse()
        print('[' + ','.join(queue) + ']')