#!/usr/bin/env python3
"""
This is a module that provides a function for summing list values
that are either integers of floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function computes the sum of a list of integers and floats, and

    Parameters: mxd_lst (List[Union[int, float]]): list of integers and floats

    Returns: float: The sum of the elements in mxd_lst.
    """
    return sum(mxd_lst)
