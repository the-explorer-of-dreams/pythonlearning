#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MetaClassTest
   Description :
   Author :       william
   date：          2018/8/9
-------------------------------------------------
   Change Activity:
                   2018/8/9:
-------------------------------------------------
"""
__author__ = 'william'


# 道生一：传入type
class SayMetaClass(type):

    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        # 创造“天赋”
        attrs['say_' + name] = lambda self, value, saying=name: print(saying + ',' + value + '!')
        # 传承三大永恒命题：类名称、父类、属性
        return type.__new__(cls, name, bases, attrs)


# 一生二：创建类
class Hello(dict, metaclass=SayMetaClass):
    parent = 'Hello parent'
    pass


class HelloChild(Hello):
    child1 = 'Hello child1'
    pass




# 二生三：创建实列
hello = HelloChild()

# 三生万物：调用实例方法

hello.say_Hello('world!')

print(hello.child1)

