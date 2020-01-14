# -*- coding:utf-8 -*-
# @Time:  2020/1/6 11:23
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  jenkins.py
# @Software:  PyCharm

# 脚本与业务分离，编写jenkins等公用方法
import requests
import urllib3
import warnings
import re
import unittest
urllib3.disable_warnings()
warnings.simplefilter('ignore',ResourceWarning)


class Jenkins():
    def __init__(self,s):
        s=requests.session()
        self.s=s

    def Login_Jenkins(self,username,passwd):
        # 登录Jenkins
        url='http://localhost:8080/jenkins/j_acegi_security_check'
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        body={'j_username': username,'j_password':passwd,'from':'','Submit': '登录',
              'remember_me':'on'}
        res=self.s.post(url,headers=head,data=body)
        return res.text

    def RenWu(self,jobname):
        # 提交任务
        url2 = 'http://localhost:8080/jenkins/user/wangyangyang/my-views/view/all/createItem'
        body2 = {'name': jobname,
                 'mode': 'hudson.maven.MavenModuleSet',
                 'from': '',
                 'Jenkins-Crumb': 'd4052370eacecaed11f21e457a931612',
                 'json': '{"name": '+jobname+', "mode":"hudson.maven.MavenModuleSet","from": "","Jenkins-Crumb":"d4052370eacecaed11f21e457a931612"}'}
        res = self.s.post(url2, data=body2)
        return res.text


if __name__=='__main__':
    unittest.main()
