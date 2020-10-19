"""
    Get the zeta value from sumatory formula upto k elements
"""
from sympy.abc import i, k, m, n, x
from sympy import Sum, factorial, oo, IndexedBase, Function

z = Sum(x**k, (k, 0, oo))
z
    
    
