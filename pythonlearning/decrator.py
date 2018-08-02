#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

def log(text='default'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            result = func(*args, **kw)
            print('called after')
            return result
        return wrapper
    return decorator

@log()
def now():
    print('20180802')
    print('self.name:%s' % now.__name__)
    return 'now_result'

print(now())
