#!/usr/bin/python3
# -*- coding: utf-8 -*-

filename = 'guest_inputed.txt'

with open(filename, 'a') as file:
    while True:
        print("Please enter your name: ")
        print("(input 'q' to quit)")
        guest_name = input("your name: ")
        if guest_name == 'q':
            break

        print("Welcome " + guest_name.title())
        file.write(guest_name + "\n")