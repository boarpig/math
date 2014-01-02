#!/usr/bin/python

def amicablePair(number):
    pairset = set()
    for i in range(number):
        n = sum(d(i))
        if i == sum(d(n)):
            if i != n:
                if i < number:
                    pairset.add(i)
                if n < number:
                    pairset.add(n)
    return list(pairset)

def d(number):
    'Returns sum of all divisors of a number'
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return divisors

#print str(sorted(lol)) + ' = ' + str(sum(lol))
