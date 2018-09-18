#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pizza
   Description :
   Author :       william
   date：          2018/9/17
-------------------------------------------------
   Change Activity:
                   2018/9/17:
-------------------------------------------------
"""
__author__ = 'william'


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
