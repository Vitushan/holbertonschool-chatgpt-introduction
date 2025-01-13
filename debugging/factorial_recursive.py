#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to compute the factorial of a given number recursively.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
