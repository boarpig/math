#!/usr/bin/python

from decimal import Decimal, Context, getcontext
from math import factorial, ceil

A = Decimal(13591409)
B = Decimal(545140134)
C = Decimal(-640320)

def chudnovsky(tarkkuus):
    getcontext().prec = tarkkuus + 2
    D = Decimal(426880) * Decimal(10005).sqrt()
    x = Decimal(ceil(tarkkuus / 12))
    dividend = Decimal(0)
    divisor = Decimal(0)
    pi = Decimal(0)
    for k in range(0, int(x) + 1):
        dividend = factorial(6 * k) * (A + B * k)
        divisor = factorial(3 * k) * factorial(k)**3 * C**(3 * k)
        pi += (dividend / divisor)
    print(str(D / pi)[:-2])

chudnovsky(1000)
