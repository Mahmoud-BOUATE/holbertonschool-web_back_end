#!/usr/bin/env python3
"""Module Async Generator"""

import asyncio
import random


async def async_generator():
    """Function that yield a ranom number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0,10))

async def main():
    async for i in async_generator():
        print(i)

asyncio.run(main())
