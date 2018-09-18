#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ice_cream_stand
   Description :
   Author :       william
   date：          2018/9/18
-------------------------------------------------
   Change Activity:
                   2018/9/18:
-------------------------------------------------
"""
__author__ = 'william'


class IceCreamStand:
    """这是一个冰淇淋小店的尝试"""

    def __init__(self, flavors):
        self.flavors = flavors

    def get_icecreamstand_flavors(self):
        """获取所有口味"""
        print("The IceCreamStand haa these flavors:")
        for flavor in flavors:
            print("\t-" + flavor)


if __name__ == "__main__":
    flavors = ['apple', 'banana', 'pear']
    ics = IceCreamStand(flavors)
    ics.get_icecreamstand_flavors()