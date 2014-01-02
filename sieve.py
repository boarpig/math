#!/usr/bin/python3

from math import sqrt

def sieve(n):
    """Takes in n and returns list containing all primes smaller than or
    equal to n. 
    
    Algorithm: Sieve of Eratosthenes
    
    """
    primelist = [1]
    numberlist = list(range(2, n+1))
    while numberlist[0] < sqrt(n):
        primelist.append(numberlist[0])
        s = 0
        while s * primelist[-1] < n:
            s += 1
            if (s * primelist[-1]) in numberlist:
                numberlist.remove(s * primelist[-1])
    for rest in numberlist:
        primelist.append(rest)
    return primelist

if __name__ == '__main__':
    print(sieve(10000))
