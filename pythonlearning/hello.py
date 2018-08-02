#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     hello.py
   Description :
   Author :       william
   date：          2018/8/2
-------------------------------------------------
   Change Activity:
                   2018/8/2:
-------------------------------------------------
"""
__author__ = 'william'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello,%s' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()