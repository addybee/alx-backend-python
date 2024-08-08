#!/usr/bin/env python3
"""
contains a function that Return the first element of a sequence safely.
"""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence safely.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Optional[Any]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
