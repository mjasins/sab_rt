"""Dummy module to test packages.

This module provides:
- add_binary - a dummy function
"""

def add_binary(a, b):
    """Return the sum of two decimal numbers in binary digits.

    Parameters
    ----------
    a : int
        A decimal integer
    b : int
        Another decimal integer

    Returns
    -------
    binary_sum : str
        Binary string of the sum of a and b
    """
    binary_sum = bin(a+b)[2:]
    return binary_sum
