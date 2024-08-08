#!/usr/bin/env python3
"""
Module: typing
Description: This module provides support for type hints.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Parameters:
    - input_list (List[float]): A list of floats to sum.

    Returns:
    - float: The sum of the input_list.

    Example:
    >>> sum_list([1.5, 2.5, 3.0])
    7.0
    """
    return sum(input_list)
