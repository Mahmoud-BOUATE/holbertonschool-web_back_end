#!/usr/bin/env python3
"""Asynchronous comprehension collecting 10 random numbers."""

from typing import List
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Run time for four parallel comprehensions"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                                   async_comprehension(),
                                   async_comprehension(),
                                   async_comprehension(),
                                   )
    end = asyncio.get_event_loop().time()
    return end - start
