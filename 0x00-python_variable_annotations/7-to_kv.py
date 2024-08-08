#!/usr/bin/env python3
"""
    Module: to_kv
    This module provides a function to Converts a key-value pair where
    the value is squared.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key-value pair where the value is squared.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value as an integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return (k, v * v)
