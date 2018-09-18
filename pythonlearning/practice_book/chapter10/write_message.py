#!/usr/bin/python3
# -*- coding: utf-8 -*-


filenamew= 'programming.txt'

with open(filenamew, 'w') as file_object:
    file_object.write("FILE WRITE:\n")
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

filenamea = 'file_add_mode.txt'

with open(filenamea, 'a') as file_object:
    file_object.write("FILE WRITE:\n")
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")