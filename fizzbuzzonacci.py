def fizzbuzzonacci(n):
    # First, generate the first n Fibonacci numbers.
    fibos = fibonacci_numbers(n)

    # Then, print lines based on their Fizz/Buzz/BuzzFizz status.
    # This implementation will print multiple things if multiple conditions obtain,
    # i.e. it prints "Buzz" and then "Fizz" (on separate lines) if a number is divisible by 3 and 5.
    for fibo in fibos:
        if prime(fibo):
            print "BuzzFizz"
            continue
        elif divisible_by(fibo, 3):
            print "Buzz"
        elif divisible_by(fibo, 5):
            print "Fizz"
        else:
            print fibo

def fibonacci_numbers(num):
    # I'm considering the Fibonacci sequence to begin with the terms 1, 1, 2, 3...
    # where the zeroth fibonacci number is meaningless, and the first is 1.
    if num == 0: return []
    if num == 1: return [1]

    fibos = [1, 1]
    while len(fibos) < num:
        fibos.append(fibos[-1] + fibos[-2])
    return fibos

def divisible_by(num, divisor):
    return num % divisor == 0

def prime(num):
    pass

fizzbuzzonacci(10)
