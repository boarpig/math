#!/usr/bin/python
#coding: utf8

from sys import argv
from math import sqrt, ceil

def isprime(n):
    """Checks given number for primality.
    Returns true and number itself if number is prime or
    false and smallest primefactor if not prime.

    Naive implementation
    
    """
    primelist = [2, 3]
    nprime = True
    prime = True
    if (n % 2) == 0:
        print("Numero on parillinen, ei alkuluku")
    if sqrt(n) % 1 == 0:
        print("Numero on neliö")
    elif n > 4:
        m = 5
        sqrtn = ceil(sqrt(n))
        while m <= sqrtn:
            sqrtm = sqrt(m)
            for i in primelist:
                if (m % i) == 0:
                    prime = False
                    break
                if i >= sqrtm:
                    break
            if prime:
                primelist.append(m)
                if (n % m) == 0:
                    nprime = False
                    break
            else:
                prime = True
            m += 2
    return nprime, m

if __name__ == '__main__':
    print(isprime(99999999977))
