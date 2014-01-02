#!/usr/bin/python

def simpson_rule(f, a, b):
    """Approximate the definite integral of f from a to b by Simpson's rule."""
    c = (b - a)/6.0
    d = (a + b)/2.0
    return c * (f(a) + 4.0 * f(d) + f(b))
