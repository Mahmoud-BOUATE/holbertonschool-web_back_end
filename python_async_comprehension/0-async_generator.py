#!/usr/bin/env python3
"""Test async_generator"""

import asyncio

# Import de la coroutine async_generator
async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    """Récupère toutes les valeurs yieldées et les affiche"""
    result = []
    async for value in async_generator():
        result.append(value)
    print(result)

# Exécution
asyncio.run(print_yielded_values())
