#!/usr/bin/python

def numberChain(x):
    '''A number chain is created by continuously adding the square of the 
    digits in a number to form a new number until it has been seen before.

    for example,

    44 -> 32 -> 13 -> 10 -> 1
    85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
    loop. What is most amazing is that EVERY starting number will eventually 
    arrive at 1 or 89.
    
    '''
    luku = x
    while luku not in (1, 89):
        yield x
        luku = x
        x = 0
        for i in str(luku):
            x += int(i)**2

if __name__ == '__main__':
	for i in numberChain(42):
		print(i)
