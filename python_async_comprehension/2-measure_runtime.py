#!/usr/bin/env python3

"""
ipmort async_comprehension from the prev file
and write a coroutine called measure_runtime
that will execute async_comprehension four times in parallel
using asyncio.gather

measure_runtime should measure the total runtime and return it
"""
import asyncio
import time
import typing
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ already described in the comment at the beginning of the file """
    before = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    after = time.time()
    total_time = after - before

    return total_time
