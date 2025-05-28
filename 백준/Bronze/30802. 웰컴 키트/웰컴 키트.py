fan = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

shrit = 0
for i in size:
    shrit += (i - 1) // t + 1

mock, unit = fan // p, fan % p

print(shrit)
print(mock, unit)