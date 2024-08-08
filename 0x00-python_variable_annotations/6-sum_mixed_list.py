#!/usr/bin/env python3
"""
    Module: sum_mixed_list
    This module provides a function to calculate the sum of a mixed list of
    integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
    - mxd_lst: A list containing integers and floats.

    Returns:
    - The sum of the elements in the mixed list as a float.
    """
    return sum(mxd_lst)
