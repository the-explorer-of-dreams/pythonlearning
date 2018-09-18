#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proconexample
   Description :
   Author :       william
   date：          2018/8/27
-------------------------------------------------
   Change Activity:
                   2018/8/27:
-------------------------------------------------
"""
__author__ = 'william'


def consumer():
    r = ''
    while True:
        product = yield r
        print('consuming the product %d' % product)
        r = '200 OK'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('sending consumer %d' % n)
        r = c.send(n)
        print('consumer return %s' % r)
    c.close()


c = consumer()
producer(c)
