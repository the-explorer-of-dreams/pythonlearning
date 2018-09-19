#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     names
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'

from name_function import get_formated_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formated_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")

