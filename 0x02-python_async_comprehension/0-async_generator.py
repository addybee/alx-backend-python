#!/usr/bin/env python3
"""
Module: async_generator_module

This module provides an asynchronous generator function `async_generator`
that yields random floating-point numbers between 0 and 10 after waiting
for 1 second asynchronously using `asyncio.sleep`.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random floating-point numbers between
    0 and 10 after waiting for 1 second asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
