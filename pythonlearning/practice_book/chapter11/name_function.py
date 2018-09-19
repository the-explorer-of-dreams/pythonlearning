#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     name_function
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'


def get_formated_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if not middle:
        full_name = first + ' ' + last
    else:
        full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

