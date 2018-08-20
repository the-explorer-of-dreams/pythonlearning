#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mysqlexample
   Description :
   Author :       william
   date：          2018/8/20
-------------------------------------------------
   Change Activity:
                   2018/8/20:
-------------------------------------------------
"""
__author__ = 'william'

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='mysql', database='mydb')
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()