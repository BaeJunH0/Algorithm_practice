import sys

input = sys.stdin.readline

def bct(depth : int, idx : int):
    # 종료 조건 : m 길이 수열이 만들어지면 종료
    if depth == m:
        print(' '.join(map(str, response)))
        return

    # 이미 정렬된 수열 탐색이므로 idx 부터 탐색하면 이후 값들은 전부 지금보다 크거나 같음
    # 중복된 값을 지웠으므로, n이 아니라 len(sequence) 사용하기
    for i in range(idx, len(sequence)):
        response.append(sequence[i])
        bct(depth + 1, i)
        response.pop()    

n, m = map(int, input().rstrip().split())

sequence = sorted(set(list(map(int, input().rstrip().split()))))
response = []

bct(0, 0)