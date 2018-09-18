#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Restaurant:
    """餐馆类，永远模拟餐馆。"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Our restaurant name is " + self.restaurant_name.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " now is open, Our cuisine is " + self.cuisine_type)


if __name__ == '__main__':
    my_restaurant1 = Restaurant('JiXiang', 'china')
    my_restaurant2 = Restaurant('cherry', 'japan')
    my_restaurant3 = Restaurant('tom', 'america')

    my_restaurant1.describe_restaurant()
    my_restaurant2.describe_restaurant()
    my_restaurant3.describe_restaurant()

