#!/usr/bin/python3
# -*- coding: utf-8 -*-

requested_toppings = []

requested_toppings.append(input('please input the favor:'))
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding '+ requested_topping + '.')
    print('\nfinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')