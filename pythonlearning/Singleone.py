#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Singleone
   Description :
   Author :       william
   date：          2018/8/9
-------------------------------------------------
   Change Activity:
                   2018/8/9:
-------------------------------------------------
"""
__author__ = 'william'


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''

    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


#  这会作用到这个模块中的所有类
class Foo(object, metaclass=upper_attr):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


hasattr(Foo, 'bar')

# 输出: False

hasattr(Foo, 'BAR')
# 输出:True

f = Foo()
print(f.BAR)
# 输出:'bip'
