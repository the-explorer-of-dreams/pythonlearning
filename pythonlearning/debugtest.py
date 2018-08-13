#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     debug
   Description :
   Author :       william
   date：          2018/8/10
-------------------------------------------------
   Change Activity:
                   2018/8/10:
-------------------------------------------------
"""
__author__ = 'william'


# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
#
# def main():
#     foo('0')
#
# main()

import logging
logging.basicConfig(level=logging.DEBUG)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# import logging  # 引入logging模块
# logging.basicConfig(level=logging.DEBUG)
# # 将信息打印到控制台上
# logging.debug(u"苍井空")
# logging.info(u"麻生希")
# logging.warning(u"小泽玛利亚")
# logging.error(u"桃谷绘里香")
# logging.critical(u"泷泽萝拉")