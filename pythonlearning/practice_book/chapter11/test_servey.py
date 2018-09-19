#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_servey
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
from servey import AnonimousServey


class AnonimousServeyTest(unittest.TestCase):
    """针对AnonimousServey进行测试"""

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonimousServey(question)
        self.responses = ['English', 'Chinese', 'Spanish']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""

        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """测试3个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_responses(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()