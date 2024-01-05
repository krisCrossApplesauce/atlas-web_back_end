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


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """ runs wait_random n times and returns a list of the results """
    lst = []
    i = 0
    d = 0

    while i < n:
        d = await wait_random(max_delay)
        for ii in range(len(lst) + 1):
            if ii == len(lst):
                lst.append(d)
            elif ii < len(lst) and d < lst[ii]:
                lst.insert(ii, d)
                break
        i += 1

    return lst
