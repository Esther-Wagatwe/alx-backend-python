#!/usr/bin/env python3
"""
This is a module that provides a function for creating a function that
    multiplies a float by a multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float as an argument and returns a function that
        multiplies a float by the multiplier.

    Parameters: multiplier (float): Use in the returned function.

    Returns: Callable[[float], float]: Function that multiplies a float by the
        multiplier.
    """
    def multiply(x: float) -> float:
        """
        This function multiplies a float by the multiplier.

        Parameters: n (float): To multiply with multiplier.

        Returns: float: The result of multiplying n by the multiplier.
        """
        return (x * multiplier)

    return multiply
