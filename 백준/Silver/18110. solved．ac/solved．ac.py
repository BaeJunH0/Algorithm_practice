import sys

def r(num): 
    # 0.49999... 까지는 올림한 값보다 작음
    if num + 0.5 < int(num) + 1:
        return int(num)
    else:
        return int(num) + 1

def solve():
    seq = int(sys.stdin.readline().strip())

    if seq == 0:
        print(0)
        exit()

    arr = []
    for i in range(seq):
        arr.append(int(sys.stdin.readline().strip()))

    arr.sort()

    bound = r((0.15) * seq)
    arr = arr[bound:seq-bound]

    answer = r(sum(arr) / len(arr))
    print(answer)

solve()