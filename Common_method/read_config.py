# -*- coding:utf-8 -*-
# @Time:  2020/1/10 11:33
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  read_config.py
# @Software:  PyCharm
import configparser
conn = configparser.ConfigParser()
conn.read('E:\\honggetest\\configure\\config.ini')


def ReadConfig(configname):
    result1=conn.items(configname)
    mydict={}
    for i in result1:
        mydict[i[0]]=i[1]
    return mydict


if __name__=='__main__':
    configname='email'
    mydict=ReadConfig(configname)
    print(mydict)


