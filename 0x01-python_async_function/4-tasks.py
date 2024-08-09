#!/usr/bin/env python3
"""
    task4 Asynchronous function that creates and awaits 'n'
    tasks with random delays up to 'max_delay'.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Perform n asynchronous tasks with a maximum delay and return a list of
    results.

    Parameters:
    - n: An integer representing the number of tasks to perform.
    - max_delay: An integer specifying the maximum delay for each task.

    Returns:
    A list of floats representing the results of the asynchronous tasks.

    Usage:
    results = await task_wait_n(5, 10)
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
