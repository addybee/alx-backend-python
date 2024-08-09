#!/usr/bin/env python3
"""
Module for the routine of the time taken to execute a task `n` times with
a maximum delay
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the time taken to execute a task `n` times with a maximum delay of
    `max_delay`.

    Parameters:
    - `n` (int): The number of times the task will be executed.
    - `max_delay` (int): The maximum delay allowed for each task execution.

    Returns:
    - float: The total time taken to execute the task `n` times.
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - start
    return total_time / n
