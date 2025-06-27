def solution(prices):
    answer = [0] * len(prices)
    stack = []
    length = len(prices)

    for i in range(length):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    for i in stack:
        answer[i] = length - 1 - i

    return answer