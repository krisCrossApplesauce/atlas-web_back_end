#!/usr/bin/env python3

"""
write a coroutine called async_generator
that takes no args

it'll loop 10 times,
each time asynchronously waiting 1 sec,
then yield a random number between 0 and 10
"""
import asyncio
import random


async def async_generator():
    """ does stuff (explained in comment at beginning of file) """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
