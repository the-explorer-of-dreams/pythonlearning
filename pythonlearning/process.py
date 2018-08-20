#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     process
   Description :
   Author :       william
   date：          2018/8/14
-------------------------------------------------
   Change Activity:
                   2018/8/14:
-------------------------------------------------
"""
from idlelib import run

__author__ = 'william'

from multiprocessing import Process
import os


#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__' :
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('child process end.')