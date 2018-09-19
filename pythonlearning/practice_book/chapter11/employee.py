#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Employee
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'


class Employee:
    """雇员类"""

    def __init__(self, first_name, last_name, year_salary):
        """类初始化函数"""
        self.first_name = first_name
        self.last_name = last_name
        self.year_salary = year_salary

    def give_raise(self, year_salary_increment=5000):
        """工资调整函数，默认加年薪5000美元"""
        self.year_salary += year_salary_increment

