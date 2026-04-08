#!/usr/bin/env python3
"""Asynchronous generator yielding random floats."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random floats between 0 and 10 with 1-second async waits."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
