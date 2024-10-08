def solve(x, y):
    return max(x) * max(y)
def solution(sizes):
    x, y = [], []
    for i in sizes:
        x.append(max(i[0], i[1]))
        y.append(min(i[0], i[1]))
        
    answer = solve(x, y)
    return answer