#!/usr/bin/python

from math import sqrt

def primeFactors(number):
    """Returns all prime factors of a number."""
    divisor = 2
    factors = [1]
    while divisor <= sqrt(number):
        if (number % divisor) == 0:
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1
    factors.append(number)
    return factors

def divisors(number):
    """Returns all divisors of the number."""
    divisors = 2
    sqrtn = int(sqrt(number))
    for i in range(2, sqrtn - 1):
        if (number % i)==0:
            divisors += 2
    if sqrtn**2 == number:
        divisors += 1
    return divisors
