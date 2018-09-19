#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     city_countries
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'


def get_formatted_city_country(city, country, population=''):
    """测试城市国家格式化字符串"""

    if population:
        formatted_city_country = city.title() + ',' + country.title() + ' - population ' + str(population)
    else:
        formatted_city_country = city.title() + ',' + country.title()

    return formatted_city_country
