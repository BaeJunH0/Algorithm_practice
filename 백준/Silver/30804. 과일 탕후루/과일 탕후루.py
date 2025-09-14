import sys
from collections import defaultdict

input = sys.stdin.readline

seq = int(input())
fruits = list(map(int, input().rstrip().split()))

window = defaultdict(int)
left, max_len = 0, 0

for right in range(0, seq):
    window[fruits[right]] += 1

    while len(window.keys()) > 2:
        window[fruits[left]] -= 1
        if window[fruits[left]] == 0:
            del window[fruits[left]]
        
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)