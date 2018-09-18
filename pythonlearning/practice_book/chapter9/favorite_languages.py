#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     favorite_languages
   Description :
   Author :       william
   date：          2018/9/18
-------------------------------------------------
   Change Activity:
                   2018/9/18:
-------------------------------------------------
"""
__author__ = 'william'

from collections import OrderedDict

favorite_luaguages = OrderedDict()

favorite_luaguages['jen'] = 'python'
favorite_luaguages['sarah'] = 'c'
favorite_luaguages['edward'] = 'ruby'
favorite_luaguages['phil'] = 'python'

for name, language in favorite_luaguages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
