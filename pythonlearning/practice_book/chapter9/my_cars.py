#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     my_cars
   Description :
   Author :       william
   date：          2018/9/18
-------------------------------------------------
   Change Activity:
                   2018/9/18:
-------------------------------------------------
"""
__author__ = 'william'


# from car import Car, ElectircCar
#
# my_beetle = Car('volkswagen', 'beetle', 2018)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectircCar('tesla', 'roadster', 2018)
# print(my_tesla.get_descriptive_name())

import car

my_beetle = car.Car('volkswagen', 'beetle', 2018)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectircCar('tesla', 'roadster', 2018)
print(my_tesla.get_descriptive_name())