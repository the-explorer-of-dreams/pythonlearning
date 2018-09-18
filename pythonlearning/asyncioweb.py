#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     asyncioweb
   Description :
   Author :       william
   date：          2018/8/24
-------------------------------------------------
   Change Activity:
                   2018/8/24:
-------------------------------------------------
"""
__author__ = 'william'

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    print('reader, writer = yield from connect')
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# tasks = [wget(host) for host in ['www.sina.com.cn']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()