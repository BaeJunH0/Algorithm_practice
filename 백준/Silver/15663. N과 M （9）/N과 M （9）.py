import sys

input = sys.stdin.readline

def bct():
    check = 0

    if len(response) == m:
        print(*response)
    
    for i in range(n):
        if check != sequence[i] and not visited[i]:
            visited[i] = True
            check = sequence[i]

            response.append(sequence[i])
            bct()

            response.pop()
            visited[i] = False

n, m = map(int, input().rstrip().split())

sequence = sorted(list(map(int, input().rstrip().split())))

response = []
visited = [False] * n
bct()