#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     aiohttpexample
   Description :
   Author :       william
   date：          2018/8/23
-------------------------------------------------
   Change Activity:
                   2018/8/23:
-------------------------------------------------
"""
__author__ = 'william'

# import asyncio
#
# from aiohttp import web
#
#
# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>', content_type='text/html')
#
#
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))
#
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

# import time
# import asyncio
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#
#
# start = now()
#
# coroutine = do_some_work(2)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
#
# print('TIME: ', now() - start)


# import asyncio
# import time
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# # task = asyncio.ensure_future(coroutine)
# task = loop.create_task(coroutine)
# print(task)
# loop.run_until_complete(task)
# print(task)
# print('TIME: ', now() - start)

# import time
# import asyncio
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#     return 'Done after {}s'.format(x)
#
#
# def callback(future):
#     print('Callback: ', future.result())
#
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# loop.run_until_complete(task)
#
# print('TIME: ', now() - start)

# import asyncio
#
# import time
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#
    # await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
#
# start = now()
#
# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(4)
#
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3)
# ]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# for task in tasks:
#     print('Task ret: ', task.result())
#
# print('TIME: ', now() - start)

# import asyncio
#
# import time
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
#
# async def main():
#     coroutine1 = do_some_work(1)
#     coroutine2 = do_some_work(2)
#     coroutine3 = do_some_work(4)
#
#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3)
#     ]
#
#     # dones, pendings = await asyncio.wait(tasks)
#     #
#     # for task in dones:
#     #     print('Task ret: ', task.result())
#
#     results = await asyncio.gather(*tasks)
#
#     for result in results:
#         print('Task ret: ', result)
#
# start = now()
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
#
# print('TIME: ', now() - start)

import asyncio

# 一个对future进行赋值的函数
async def slow_operation(future):
    print('slow_operation')
    await asyncio.sleep(5)
    # 给future赋值
    future.set_result('Future is done!')


# async def fast_operation():
#     print('fast_operation')
#     # await asyncio.sleep(5)
#     await fast_operation_01()

@asyncio.coroutine
def fast_operation():
    print('fast_operation')
    # await asyncio.sleep(5)
    n = yield from fast_operation_01()
    print('n',n)


async def middle_operation():
    print('middle_operation')
    # await fast_operation()


async def fast_operation_01():
    print('fast_operation_01')
    # await asyncio.sleep(5)
    return 'fast_operation_01 return'
loop = asyncio.get_event_loop()
# # 创建一个future
# future1 = asyncio.Future()
# # 使用ensure_future 创建Task
# asyncio.ensure_future(slow_operation(future1))
# future2 = asyncio.Future()
# asyncio.ensure_future(slow_operation(future2))
# asyncio.ensure_future(fast_operation())

loop.create_task(fast_operation())



# gather Tasks，并通过run_uniti_complete来启动、终止loop
loop.run_until_complete(middle_operation())
# loop.run_until_complete()
# loop.run_forever()

# print(future1.result())
# print(future2.result())
# loop.close()