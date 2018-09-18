#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     file_reader
   Description :
   Author :       william
   date：          2018/9/18
-------------------------------------------------
   Change Activity:
                   2018/9/18:
-------------------------------------------------
"""
__author__ = 'william'

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)
#     print("---end---")

# with open('pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())