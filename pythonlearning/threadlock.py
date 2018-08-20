#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     threadlock
   Description :
   Author :       william
   date：          2018/8/16
-------------------------------------------------
   Change Activity:
                   2018/8/16:
-------------------------------------------------
"""
__author__ = 'william'

import time
import threading
from multiprocessing import Process
import os

# account balance
# balance = 0


# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print('balance=%s' % balance)


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(4):
    # t = threading.Thread(target=loop)
    # print('the %d thread is running.' % i)
    p = Process(target=loop)
    print('the %d process is running.' % os.getpid())
    p.start()

