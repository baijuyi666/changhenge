# -*- coding:utf-8 -*-
# @Time:  2020/1/3 11:25
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  test_04.py
# @Software:  PyCharm

import requests
import unittest
import time
import re
import urllib3
import warnings
from case.method.jenkins import Jenkins


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        print("start")
        urllib3.disable_warnings()
        warnings.simplefilter("ignore", ResourceWarning)
        s=requests.session()
        self.Jenkins=Jenkins(s)

    def tearDown(self) -> None:
        time.sleep(1)
        print("end!")

    def test_004_Add(self):
        print('运行第四条用例，加法运算')
        result=5+5
        hope=11
        self.assertNotEqual(result,hope)

    def test_005_loginJenkins(self):
        # 运行第五条用例，登录Jenkins
        username = 'wangyangyang'
        passwd = 'jiale8897'
        res=self.Jenkins.Login_Jenkins(username = 'wangyangyang',passwd = 'jiale8897')
        result1 = re.findall(u'<b>(.*?)</b></a>', res)[1]
        hope = '注销'
        self.assertEqual(result1, hope, msg='断言失败，请检查预期和实际结果！')

    def test_006_job(self):
        self.Jenkins.Login_Jenkins(username = 'wangyangyang',passwd = 'jiale8897')
        jobname='山河999'
        res=self.Jenkins.RenWu(jobname)
        result=re.findall(u'<title>(.+?) Config',res)[0]
        print(result)
        self.assertEqual(result,"山河999")


if __name__ == '__main__':
    unittest.main()


