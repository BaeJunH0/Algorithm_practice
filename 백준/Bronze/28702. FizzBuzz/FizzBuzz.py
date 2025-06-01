def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

arr = [input() for i in range(3)]
target = 0

for i in range(3):
    if arr[i].isdigit():
        target = int(arr[i]) + (3 - i) 

fizzbuzz(target)