# -*- coding:utf-8 -*-
# @Time:  2020/1/3 17:12
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  send_mail.py
# @Software:  PyCharm
import zmail
import os


# 找出最新的测试报告
def new_file():
    for root,dirs,files in os.walk('E:\\honggetest\\report'):
        new_set=sorted(set(files))
    print(new_set[-1])
    return new_set[-1]

new_file()
new_file=new_file()
# 准备发送给对方的邮件标题，正文和附件
print("发送邮件")
Mail_Content={"subject":"这是标题",
              "content_text":"这是正文",
              "attachments":"E:\\honggetest\\report\\"+new_file+""}
# 发送方账号和密码（此密码是授权码）
server=zmail.server("1976572326@qq.com","pmiwewssvuzvbcja")
# 收件方账号和给对方发的内容
server.send_mail("1976572326@qq.com",Mail_Content)

