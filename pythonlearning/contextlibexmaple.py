#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     contextlibexmaple
   Description :
   Author :       william
   date：          2018/8/17
-------------------------------------------------
   Change Activity:
                   2018/8/17:
-------------------------------------------------
"""
__author__ = 'william'

# class Query(object):
#
#     def __init__(self, name):
#         print('__init__')
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#
# if __name__ == '__main__':
#     with Query('Bob') as q:
#         q.query()

from contextlib import contextmanager


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


if __name__ == '__main__':
    with create_query('Bob') as q:
        print('q.query()')
        q.query()