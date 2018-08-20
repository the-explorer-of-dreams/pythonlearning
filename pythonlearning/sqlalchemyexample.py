#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sqlalchemy
   Description :
   Author :       william
   date：          2018/8/20
-------------------------------------------------
   Change Activity:
                   2018/8/20:
-------------------------------------------------
"""
__author__ = 'william'

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#base domain
Base = declarative_base()


#define User
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))


#initial connection information
engine = create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/mydb')
#dbsession config
DBSession = sessionmaker(bind=engine)

# #create session
# session = DBSession()
# #create user
# new_user = User(id=5, name='Bob')
# #add user to session
# session.add(new_user)
# #commit to db
# session.commit()
# #close session
# session.close()


# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
print('books = %s' % user.books)
# 关闭Session:
session.close()

