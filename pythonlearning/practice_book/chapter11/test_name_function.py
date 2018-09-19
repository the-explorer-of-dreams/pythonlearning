#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_name_function
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
from name_function import get_formated_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formated_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle(self):
        """测试3部分名字"""
        format_name = get_formated_name('wang', 'qing', 'guo')
        self.assertEqual(format_name, 'Wang Guo Qing')

if __name__ == '__main__':
    unittest.main()