fac = [1]

n = int(input())
count = 1
while fac[-1] < n:
    fac.append(fac[-1] * count)
    count += 1
fac = fac[::-1]

def solve(n, fac):
    if n == 0:
        return 'NO'
    for i in fac:
        if n - i >= 0:
            n -= i

        if n == 0:
            return 'YES'
    return 'NO'

print(solve(n, fac))