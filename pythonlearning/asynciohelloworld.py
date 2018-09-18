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

def gen_one():
    subgen1 = range(2)
    yield from subgen1
    subgen2 = range(3)
    yield from subgen2
    return 5


def gen_two():
    subgen = range(10)
    for item in subgen:
        yield item

#
# def gen():
#     yield from subgen()
#
# def subgen():
#         while True:
#             x = yield
#             yield x+1
#
# def main():
#         g = gen()
#         next(g)
#         retval = g.send(1)
#         print(retval)
#         g.throw(StopIteration)




if __name__ == '__main__':
    one = gen_one()
    one.send(None)
    print(next(one))
    # print(next(one))
    # print(next(one))
    # print(next(one))
    # print(next(one))
    # print(next(one))
    # print(next(one))


