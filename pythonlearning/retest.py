#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     retest
   Description :
   Author :       william
   date：          2018/8/16
-------------------------------------------------
   Change Activity:
                   2018/8/16:
-------------------------------------------------
"""
__author__ = 'william'

import re
# test = '010 12345'
# if re.match(r'^\d{3}\-\d{3,8}', test):
#     print('ok')
# else:
#     print('failed')

test = 'someo1322ne@gmail.com'
if re.match(r'\w+@\w+\.(com|org|net)', test):
    print('ok')
else:
    print('failed')