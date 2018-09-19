#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_employee
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
from employee import Employee


class EmployeeTest(unittest.TestCase):
    """Employee测试类"""

    def setUp(self):
        self.employee = Employee('william', 'wang', 100000)

    def test_give_default_raise(self):
        """give a default raisement"""
        self.employee.give_raise()
        self.assertEqual(self.employee.year_salary, 105000)

    def test_give_custom_raise(self):
        """give a default raisement"""
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.year_salary, 108000)