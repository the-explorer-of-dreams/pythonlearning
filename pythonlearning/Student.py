#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Student
   Description :
   Author :       william
   date：          2018/8/2
-------------------------------------------------
   Change Activity:
                   2018/8/2:
-------------------------------------------------
"""
__author__ = 'william'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_name_and_score(self):
        print('name:score=%s:%d' % (self.__name, self.__score))

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

