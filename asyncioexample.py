#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     asyncioexams
   Description :
   Author :       william
   date：          2018/8/20
-------------------------------------------------
   Change Activity:
                   2018/8/20:
-------------------------------------------------
"""
__author__ = 'william'

# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     r = yield from asyncio.sleep(5)
#     print("Hello world")
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(3)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
print(threading.currentThread())
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()