#!/usr/bin/python3
# -*- coding: utf-8 -*-

number_list = list(range(1, 10))

if number_list:
    for num in number_list:
        if num % 10 == 1:
            print('The number is ' + str(num) + 'st!')
        elif num % 10 == 2:
            print('The number is ' + str(num) + 'nd!')
        elif num % 10 == 3:
            print('The number is ' + str(num) + 'rd!')
        else:
            print('The number is ' + str(num) + 'th!')
else:
    print('We need some numbers to display.')
