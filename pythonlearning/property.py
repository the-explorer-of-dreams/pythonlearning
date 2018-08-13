#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     property
   Description :
   Author :       william
   date：          2018/8/7
-------------------------------------------------
   Change Activity:
                   2018/8/7:
-------------------------------------------------
"""
from builtins import object

__author__ = 'william'


# class Student(object):
#     def set_score(self, score):
#         if not isinstance(score, int):
#             raise ValueError('score must be integer')
#         if score > 100 or score < 0:
#             raise ValueError('score must between 0 - 100')
#         self.__score = score
#
#     def get_socre(self):
#         return self.__score

# s = Student();
#
# s.set_score(980)
#
# print('Student s.score = %d ' % s.get_socre())

class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer')
        if score > 100 or score < 0:
            raise ValueError('score must between 0 - 100')
        self.__score = score


s = Student()
s.score = 55
print('Student s.score = %d ' % s.score)

#practice example


class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        self.__height = value


sc = Screen()
sc.width = 100
sc.height = 200
print('screen\'s width = %d and height = %d' % (sc.width, sc.height))

