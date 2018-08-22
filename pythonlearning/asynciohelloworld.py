#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     asynciohelloworld
   Description :
   Author :       william
   date：          2018/8/21
-------------------------------------------------
   Change Activity:
                   2018/8/21:
-------------------------------------------------
"""
__author__ = 'william'

import asyncio
import threading
async def hello_world():
    print('hello_world: %s ' % threading.current_thread())
    print("Hello World!")

print('main: %s ' %  threading.current_thread())
asyncio.run(hello_world())