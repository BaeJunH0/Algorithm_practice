def n_digit(n, number):
    response = ''
    while number >= n:
        response += str(number % n)
        number //= n
    response += str(number)
    return response[::-1]

def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(n, k):
    # k진수로 변환
    trans_n = n_digit(k, n)
    # 검증을 할 수들을 추리기
    temp = trans_n.split('0')
    target = []
    for i in temp:
        if i != '':
            target.append(int(i))
                
    answer = 0
    for i in target:
        if is_prime(i):
            answer += 1
    return answer