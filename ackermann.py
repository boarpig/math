#!/usr/bin/python

import sys

def A(m ,n):
    """Performs Ackermann function for non-negative integers m and n.
    Function itself should be self-explanatory. If you really must do bigger
    than m > 3, you'll have to increase the default recursion limit with
    sys.setrecursionlimit() function.

    """
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return A(m-1,1)
    elif m > 0 and n > 0:
        return A(m-1,A(m, n-1))
