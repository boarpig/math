#!/usr/bin/python

def gridTraverse(grid):
    """Takes a two integer tuple and returns a number how many different ways 
    it is possible to traverse from upper left corner to lower right corner.
    
    """
    luku = range(0,grid[0]+2)
    for i in range(grid[1]-1):
        for n, adder in enumerate(luku):
            if n == 0:
                n += 1
            else:
                luku[n] += luku[n-1]
    return luku[-1]
