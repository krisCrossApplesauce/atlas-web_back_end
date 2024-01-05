#!/usr/bin/env python3

"""
write an asynchronous coroutine named wait_random--
that takes in an int arg called max_delay, with a default value of 10
--that waits for a random delay between 0
and max_delay (included and float value) seconds
and eventually returns it
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ delays for a random number of seconds
    within the range of 0 and max_delay
    before returning the value of the delay (a float) """
    d = random.uniform(0, max_delay)
    await asyncio.sleep(d)
    return d
