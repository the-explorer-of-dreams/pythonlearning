#!/usr/bin/python3
# -*- coding: utf-8 -*-

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry file does not exist")