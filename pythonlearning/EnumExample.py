#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     EnumExample
   Description :
   Author :       william
   date：          2018/8/7
-------------------------------------------------
   Change Activity:
                   2018/8/7:
-------------------------------------------------
"""
__author__ = 'william'

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

