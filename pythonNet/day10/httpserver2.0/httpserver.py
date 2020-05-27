#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : httpserver.py
    @Software    : PyCharm
    @Create Time : 2020/5/26 3:09 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: httpserver v2.0
                    io并发处理
                    基本的request解析
                    使用类封装
  
"""
from socket import *
from select import select


# 将具体http server功能封装
class HTTPServer:
    def __init__(self, server_addr, static_dir):
        # 添加属性
        self.server_addr = server_addr
        self.static_dir = static_dir
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.server_addr)
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("listen the port %d" % self.port)
        self.rlist.append(self.sockfd)

        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("connect from ", addr)
                    self.rlist.append(c)
                else:
                    # 处理浏览器请求
                    self.handler(r)

    # 处理客户端请求
    def handler(self, connfd):
        # 接收http请求
        request = connfd.recv(4096)
        # 防止浏览器断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 请求解析
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername(), ':', info)
        # info分为访问网页和其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)
        self.rlist.remove(connfd)
        connfd.close()

    # 处理网页
    def get_html(self, connfd, info):
        if info == '/':
            # 网页文件
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + info

        try:
            fd = open(filename)
        except Exception:
            # 没有网页
            responseHeaders = 'HTTP/1.1 404 NotFound\r\n'
            responseHeaders += '\r\n'
            responseBody = "<h1>Sorry ,Not Found the page</h1>"
        else:
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            responseBody = fd.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    # 其他情况
    def get_data(self, connfd, info):
        # 没有网页
        responseHeaders = 'HTTP/1.1 200 OK\r\n'
        responseHeaders += '\r\n'
        responseBody = "<h1>Waiting httpserver 3.0</h1>"
        response = responseHeaders + responseBody
        connfd.send(response.encode())


# 如何使用HTTPServer类
if __name__ == '__main__':
    # 用户自己决定：地址，内容
    # 服务器地址
    server_addr = ('0.0.0.0', 8000)
    # 网页存放位置
    static_dir = './static'
    # 生成实例对此昂
    httpd = HTTPServer(server_addr, static_dir)
    # 启动服务
    httpd.server_forever()
