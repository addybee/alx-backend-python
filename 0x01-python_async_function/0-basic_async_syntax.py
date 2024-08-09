#!/usr/bin/env python3
"""
Module for asynchronous functions related to waiting for random time delays.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time within the specified maximum delay.

    Parameters:
    - max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
    - float: The randomly generated delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
