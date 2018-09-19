#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     language_servey
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'

from servey import AnonimousServey

# 定义一个问题，并创建一个表示调查的AnonymousServey对象
question =  "What language did you first learn to speak?"
my_servey = AnonimousServey(question)

# 显示问题并存储答案
my_servey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break

    my_servey.store_responses(response)

# 显示调查结果
print("\nThank you to everyone who participated in the servey!")
my_servey.show_results()