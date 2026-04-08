#!/usr/bin/env python3
"""Asynchronous comprehension collecting 10 random numbers."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of 10 random numbers from async_generator"""
    result: List[float] = []
    count = 0

    async for i in async_generator():
        result.append(i)
        count += 1
        if count == 10:
            break

    return result
