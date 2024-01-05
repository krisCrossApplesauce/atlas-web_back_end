#!/usr/bin/env python3

"""
import async_generator from the prev task
and then write a coroutine called async_comprehension
that takes no args

the coroutine will collect 10 random nums
using an async comprehensing over async_generator,
then return the 10 random numbers
"""
import asyncio
import random
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """ returns a list of 10 random numbers generated from async_generator """
    lst = []
    async for i in async_generator():
        lst.append(i)
    return lst
