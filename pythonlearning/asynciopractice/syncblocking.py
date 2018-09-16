#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import socket
#
# def blocking_way():
#     sock = socket.socket()
#     #blocking
#     sock.connect(('www.sina.com.cn', 80))
#     request = 'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'
#     sock.send(request.encode('ascii'))
#     response = b''
#     chunk = sock.recv(4096)
#     while chunk:
#         response += chunk
#         #blocking
#         chunk = sock.recv(4096)
#     return response
#
# def sync_way():
#     res = []
#     for i in range(10):
#         res.append(blocking_way())
#     return len(res)
#
# if __name__ == '__main__':
#     sync_way()


import socket


url = 'www.sina.com.cn'
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((url, port))
request_url = 'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'
sock.send(request_url.encode())
response = b''
rec = sock.recv(1024)
while rec:
    response += rec
    rec = sock.recv(1024)
