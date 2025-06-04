import sys

input = sys.stdin.readline

length, find = map(int, input().rstrip().split())

dic = {}
for i in range(length):
    site, pw = input().rstrip().split(' ')
    dic[site] = pw

for i in range(find):
    print(dic[input().rstrip()])