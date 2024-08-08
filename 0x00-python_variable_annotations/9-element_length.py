#!/usr/bin/env python3
"""
Module: element_length
Description: This module defines a function to calculate the length of elements
in an iterable of sequences.

Parameters:
    - lst: An iterable of sequences for which the length of each element
    will be calculated.
Returns: A list of tuples where each tuple contains a sequence from the input
    iterable and its corresponding length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
