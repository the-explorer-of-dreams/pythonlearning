#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     psutil
   Description :
   Author :       william
   date：          2018/8/17
-------------------------------------------------
   Change Activity:
                   2018/8/17:
-------------------------------------------------
"""
__author__ = 'william'

import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())

print(psutil.cpu_percent(interval=1, percpu=True))

print( psutil.net_if_addrs())
print(psutil.net_connections())