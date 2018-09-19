#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_cities
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'

import unittest
from city_functions import get_formatted_city_country


class CityTestCase(unittest.TestCase):
    """ 测试get_formatted_city_country函数"""

    def test_get_formatted_city_country(self):
        """测试函数"""
        formatted_city = get_formatted_city_country('chengdu', 'china')
        print(formatted_city)
        self.assertEqual(formatted_city, 'Chengdu,China')

    def test_get_formatted_city_country_population(self):
        """测试函数包含人口参数"""
        formatted_city = get_formatted_city_country('chengdu', 'china', 50000)
        print(formatted_city)
        self.assertEqual(formatted_city, 'Chengdu,China - population 50000')