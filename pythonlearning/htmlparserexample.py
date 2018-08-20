#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     htmlparserexample
   Description :
   Author :       william
   date：          2018/8/17
-------------------------------------------------
   Change Activity:
                   2018/8/17:
-------------------------------------------------
"""
__author__ = 'william'

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    context_data = ''
    pass
    # def handle_starttag(self, tag, attrs):
    #     print('<%s>' % tag)
    #
    # def handle_endtag(self, tag):
    #     print('</%s>' % tag)
    #
    # def handle_startendtag(self, tag, attrs):
    #     print('<%s/>' % tag)
    #
    def handle_data(self, data):
        self.context_data += data
        # print(data)
    #
    # def handle_comment(self, data):
    #     print('<!--', data, '-->')
    #
    # def handle_entityref(self, name):
    #     print('&%s;' % name)
    #
    # def handle_charref(self, name):
    #     print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

print(parser.context_data)







