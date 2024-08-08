#!/usr/bin/env python3
""""""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that multiplies a given number by a specified multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the input and the multiplier.
    """
    def multiply(multi: float) -> float:
        """Multiply the input by the specified multiplier.

        Args:
            multi (float): The number to multiply.

        Returns:
            float: The product of the input and the multiplier.
        """
        return multiplier * multi

    return multiply
