#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     requestsexample
   Description :
   Author :       william
   date：          2018/8/17
-------------------------------------------------
   Change Activity:
                   2018/8/17:
-------------------------------------------------
"""
__author__ = 'william'

# import requests
#
# r = requests.get('https://www.baidu.com', params={'q': 'python', 'cat': '1001'})
# print(r.url)
# print(r.status_code)
# print(r.text)
# print(r.content)
# print(r.encoding)
# print(r.json())

import chardet

print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))