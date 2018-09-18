#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     my_electric_car
   Description :
   Author :       william
   date：          2018/9/18
-------------------------------------------------
   Change Activity:
                   2018/9/18:
-------------------------------------------------
"""
__author__ = 'william'


from car import ElectircCar

my_tesla = ElectircCar('tesla', 'model s', 2018)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()