#!/usr/bin/env python3
"""
this module holds the function that Measure the total runtime for executing
async_comprehension multiple times concurrently.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension multiple
    times concurrently.

    This function starts a timer, creates multiple tasks using
    asyncio.create_task to run async_comprehension
    concurrently, waits for all tasks to complete using asyncio.gather,
    and then calculates the total runtime
    by subtracting the start time from the end time.

    Returns:
        float: Total runtime in seconds for executing async_comprehension
        multiple times concurrently.
    """
    start = time.perf_counter()  # Start the timer
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)  # Run async_comprehension concurrently
    return time.perf_counter() - start  # Calculate & return the total runtime
