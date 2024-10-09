def solution(s):
    # s의 길이가 홀수이면 짝을 지을 수 없음, 종료 조건 1
    if len(s) % 2 == 1:
        return 0
    # 종료 조건 2
    stack = []
    for i in s:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    return 0