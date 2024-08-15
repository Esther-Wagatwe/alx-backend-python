#!/usr/bin/env python3
"""
This is a module that provides a function for creating a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string and an int or float, and returns a tuple

    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The int or float to square.

    Returns: Tuple[str, float]: A tuple (k, v**2)
    """
    return (k, float(v ** 2))
