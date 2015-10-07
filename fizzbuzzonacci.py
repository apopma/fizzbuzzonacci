import math

def fizzbuzzonacci(n):
    """
    Generate the first n Fibonacci numbers and print their Fizz/Buzz status:
    "BuzzFizz" if prime, "Buzz" if divisible by 3, and "Fizz" if divisible by 5.
    Multiple lines will be printed if a number meets multiple conditions;
    i.e. 3 will print BuzzFizz and Buzz: it is prime and divisible by 3.

    >>> fizzbuzzonacci(10)
    1
    1
    BuzzFizz
    BuzzFizz
    Buzz
    BuzzFizz
    Fizz
    8
    BuzzFizz
    Buzz
    34
    Fizz
    """

    if type(n) is not int: return None

    fibos = fibonacci_numbers(n)
    for fibo in fibos:
        prime = is_prime(fibo)
        mod3 = divisible_by(fibo, 3)
        mod5 = divisible_by(fibo, 5)

        if prime: print "BuzzFizz"
        if mod3:  print "Buzz"
        if mod5:  print "Fizz"

        if (prime or mod3 or mod5) is False:
            print fibo

def fibonacci_numbers(num):
    """
    Generate an array of the first 'num' Fibonacci numbers, starting with [1, 1, 2...]
    Returns blank array for input less than 1.

    >>> fibonacci_numbers(10)
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fibonacci_numbers(0)
    []
    """

    if num == 0: return []
    if num == 1: return [1]

    fibos = [1, 1]
    while len(fibos) < num:
        fibos.append(fibos[-1] + fibos[-2])
    return fibos

def divisible_by(num, divisor):
    """
    Returns a boolean: is 'num' divisible by 'divisor' without any remainder?
    Returns False if divisor is 0 instead of raising a ZeroDivisionError.
    >>> divisible_by(100, 10)
    True
    >>> divisible_by(25, 5)
    True
    >>> divisible_by(17, 6)
    False
    >>> divisible_by(100, 0)
    False
    """

    if divisor is 0: return False
    return num % divisor == 0

def is_prime(n):
    """
    Checks whether or not an integer n is prime. Adapted from 'euler/euler10',
    which was itself adapted from a Stack Overflow answer.
    >>> is_prime(0)
    False
    >>> is_prime(2)
    True
    >>> is_prime(100)
    False
    >>> is_prime(7919)
    True
    """

    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
