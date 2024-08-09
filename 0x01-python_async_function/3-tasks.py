#!/usr/bin/env python3
"""
    this Module function Create a task to wait for a random amount of time.

"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task to wait for a random amount of time.

    Parameters:
    - max_delay: An integer representing the maximum delay time.

    Returns:
    - An asyncio.Task object representing the task created to wait
    for a random amount of time.
    """
    return asyncio.create_task(wait_random(max_delay))
