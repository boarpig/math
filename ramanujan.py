#!/usr/bin/python

from decimal import Decimal, Context, getcontext
from math import ceil

def fact(n):
    """Performs n!, meaning 1*2*3*...*n"""
    s = 1
    for i in range(1, n+1):
        s *= i
    return Decimal(s)

def ramanujan(k):
    """Calculate pi up till k decimals using Ramanujan algorithm.
    
    For real scientific purposes, you might try k=40 which is more than 
    enough for almost any imaginable scientific calculation.
    
    """
    #set constants
    A = Decimal("1103.0")
    B = Decimal("26390.0")
    C = Decimal("396.0")
    D = Decimal("9801.0")
    #initialize values
    getcontext().prec = k + 8
    sqrt2 = Decimal(2).sqrt()
    k = Decimal(int(ceil(k / 8.0) + 1))
    dividend = Decimal(0)
    divisor = Decimal(0)
    pi = Decimal(0)
    #actual calculus
    for x in range(int(k + 1)):
        dividend = fact(4 * x) * (A + B * x)
        divisor = ((fact(x))**4) * (C**(4 * x))
        pi += (dividend / divisor)
    pi = str(1 / ((2 * sqrt2 / D) * pi))
    return pi[:-8]

if __name__ == '__main__':
    print(ramanujan(10000))

# python3.2 : viidellä yrityksellä noin 10,7 sekuntia keskimäärin
# python3.3 : viidellä yrityksellä noin 0.43 sekuntia keskimäärin
# = 25x nopeutus!

