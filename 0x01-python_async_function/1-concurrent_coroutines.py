#!/usr/bin/env python3
"""
Module for asynchronous functions related to waits for `n` random delays
with a maximum delay
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for `n` random delays with a maximum delay of
    `max_delay`.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay value for each random delay.

    Returns:
        List[float]: A sorted list of floats representing the random delays
        waited for.
    """
    r1: List[float]

    r1 = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(r1)
