#!/usr/bin/env python3
"""
This module describe a function that Asynchronously generates a list
comprehension using values from async_generator.
"""
import asyncio

# Importing async_generator from '0-async_generator' module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """
    Asynchronously generates a list comprehension using values from
    async_generator.

    Returns:
        list: A list containing values generated asynchronously from
        async_generator.
    """
    return [i async for i in async_generator()]
