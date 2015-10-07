def fizzbuzzonacci(n):
    # First, generate the first n Fibonacci numbers.
    fibos = fibonacci_numbers(n)

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
    pass

def is_prime(num):
    pass
