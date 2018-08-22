#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     asynciodisplaydate
   Description :
   Author :       william
   date：          2018/8/21
-------------------------------------------------
   Change Activity:
                   2018/8/21:
-------------------------------------------------
"""
__author__ = 'william'

# import asyncio
# import datetime
# import threading
#
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         print('display_date: %s ' % threading.current_thread())
#         await asyncio.sleep(1)
#
# print('main: %s ' % threading.current_thread())
# asyncio.run(display_date())


import threading
import asyncio
from datetime import datetime

maxstarttime = None


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # yield from asyncio.sleep(5)
    for i in range(200000000):
        pass
    print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def loopmax1():
    print('loopmax1 (%s)' % threading.currentThread())
    print('loopmax1 loop start')
    for i in range(100000):
        pass
    print('loopmax1 loop end')
    global maxstarttime
    maxstarttime = datetime.now()
    yield from asyncio.sleep(1)
    print('loopmax1 wake up :',datetime.now() - maxstarttime)

    print('loopmax1 again! (%s)' % threading.currentThread())

@asyncio.coroutine
def loopmax2():
    print('loopmax2(%s)' % threading.currentThread())
    print('loopmax2 loop start')
    for i in range(200000000):
        pass
    print('loopmax2 loop end')

    yield from asyncio.sleep(3)
    print('loopmax2 again! (%s)' % threading.currentThread())

print('main: %s ' % threading.current_thread())
loop = asyncio.get_event_loop()
# print(loop)
tasks = [hello(), loopmax1(), loopmax2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# def g1():
#     yield range(5)
#
#
# def g2():
#     yield from range(5)
#
#
# it1 = g1()
# it2 = g2()
# for x in it1:
#     print(x)
#
# for x in it2:
#     print(x)
# def fab(max):
# #     n, a, b = 0, 0, 1
# #     while n < max:
# #         yield b
# #         # print b
# #         a, b = b, a + b
# #         n = n + 1
# #
# # #
# # # f = fab(5)
# # #
# # # print(next(f))
# #
# # def f_wrapper(fun_iterable):
# #     print('start')
# #     for item  in fun_iterable:
# #         yield item
# #     print('end')
# #
# #
# # wrap = f_wrapper(fab(5))
# # for i in wrap:
# #     print(i,end=' ')


# import asyncio,random
# @asyncio.coroutine
# def smart_fib(n):
#     index = 0
#     a = 0
#     b = 1
#     while index < n:
#         sleep_secs = random.uniform(0, 1)
#         yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
#         print('Smart one think {} secs to get {}'.format(sleep_secs, b))
#         a, b = b, a + b
#         index += 1
#
# @asyncio.coroutine
# def stupid_fib(n):
#     index = 0
#     a = 0
#     b = 1
#     while index < n:
#         sleep_secs = random.uniform(0, 0.5)
#         yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
#         print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
#         a, b = b, a + b
#         index += 1
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [
#         smart_fib(10),
#         stupid_fib(10),
#     ]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print('All fib finished.')
#     loop.close()