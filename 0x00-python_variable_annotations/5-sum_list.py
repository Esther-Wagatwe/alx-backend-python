#!/usr/bin/env python3
"""A module that contains a type annotated function for summing list values."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function adds two numbers and returns the result.

    Parameters: List of floats

    Returns: float: The sum of the list.
    """
    return sum(input_list)
