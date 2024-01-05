#!/usr/bin/env python3

"""
import wait_random from the previous python file and
write an async routine called wait_n
that takes in 2 int args called n and max_delay.
it will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays ordered in ascending order
without using sort() bc of concurrency.
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ runs wait_random n times and returns a list of the results """
    lst = []
    i = 0

    while i < n:
        lst.append(await wait_random(max_delay))
        i += 1

    return lst
