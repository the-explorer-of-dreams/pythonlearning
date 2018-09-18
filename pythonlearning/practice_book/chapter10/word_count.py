#!/usr/bin/python3
# -*- coding: utf-8 -*-


def count_words(filename):
    """计算一个文件大致包含多少个单词"""

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("The file does not exist.")
    else:
        # 文件已读取数据，开始统计
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


if __name__ == '__main__':
    count_words('guest_inputed.txt')