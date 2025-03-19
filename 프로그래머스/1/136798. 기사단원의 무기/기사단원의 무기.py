def counting(number):
    if number == 1:
        return 1
    answer = 1
    count = 0
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            answer += 1
        if (number // i) ** 2 == number:
            count += 1
    return answer * 2 - count
def solution(number, limit, power):
    answer = 0
    knight = [i for i in range(1, number + 1)]
    for i in knight:
        temp = counting(i)
        if temp > limit:
            temp = power
        answer += temp
    return answer