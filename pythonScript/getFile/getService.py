#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import paramiko
from scp import SCPClient
import time


class Host:
    def __init__(self, user, ip, password):
        self.user = user
        self.ip = ip
        self.password = password

    def mkdir_and_upload(self, local_path):
        try:
            # 创建ssh连接
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, username=self.user, password=self.password)

            # 连接成功后再赋予文件名
            timeStr = timeName()
            # 此处路径必须在指定服务器上有
            remote_path = "/opt/jenkins/workspace/" + timeStr

            # 创建sfp连接
            sftp = ssh.open_sftp()
            sftp.mkdir(remote_path)
            print("Create folder " + timeStr + " in remote hosts successfully!\n")

            # 创建传送文件对象
            scpclient = SCPClient(ssh.get_transport(), socket_timeout=30.0)
            try:
                scpclient.put(local_path, remote_path)
            except FileNotFoundError as e:
                print(e)
                print("找不到指定文件" + local_path)
            else:
                print("文件上传成功")

            ssh.close()
            # return createName
        except:
            print("Create folder failure!\n")


def str_to_list(url, str_name):
    """
    配置文件读取
    :param url:配置文件路径
    :param str_name:配置文件名称
    :return:
    """
    os.chdir(url)
    data = open(str_name)
    dic = []
    for line in data:
        line = line.strip('\n')
        line = line.split(":")
        if line is not None:
            dic.append(line)
    data.close()
    return dic


def timeName():
    """
    创建名
    :return:
    """
    timeStr = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    return timeStr


if __name__ == '__main__':
    # 配置文件地址
    # 配置文件名称
    # dic = str_to_list(sys.argv[1], sys.argv[2])
    dic = str_to_list("/Users/apple/PycharmProjects/tarena/month01/pythonScript/getFile", "serviceIp")
    for host_new in dic:
        # 创建host对象
        host = Host(host_new[0], host_new[1], host_new[2])

        # 传入本地文件路径
        # host.mkdir_and_upload(sys.argv[3])
        host.mkdir_and_upload("/Users/apple/PycharmProjects/tarena/month01/pythonScript/getFile/someOne.jar")
        print(host.ip+"已经完成上传")
    print("上传完成")
