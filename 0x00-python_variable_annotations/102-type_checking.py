#!/usr/bin/env python3
"""
This module provides a function to zoom in on the elements of a tuple by
repeating each element a specified number of times.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the elements of a tuple by repeating each element a specified
    number of times.

    Args:
        lst (Tuple): The input tuple to zoom in on.
        factor (int): The factor by which to zoom in on the tuple elements.
        Default is 2.

    Returns:
        List: A list containing the zoomed-in elements of the input tuple.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
