from itertools import permutations

def is_decimal(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    integer_numbers = [i for i in numbers]
    possible_numbers = []
    
    for i in range(len(integer_numbers)):
        temp = []
        if i == len(integer_numbers) - 1:
            temp = list(map(''.join, permutations(integer_numbers)))
        else:
            temp = list(map(''.join, permutations(integer_numbers, i + 1)))
        
        for j in temp:
            possible_numbers.append(int(j))
    
    possible_numbers = list(set(possible_numbers))
    print(possible_numbers)
    
    answer = 0
    for i in possible_numbers:
        if is_decimal(i):
            answer += 1
    
    return answer