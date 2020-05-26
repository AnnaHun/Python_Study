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


# 将具体http server功能封装
class HTTPServer:
    pass


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
