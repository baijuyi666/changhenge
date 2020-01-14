# -*- coding:utf-8 -*-
# @Time:  2020/1/3 11:25
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  test_02.py
# @Software:  PyCharm

import requests
import unittest
import time
import re
import urllib3
import warnings
s = requests.session()


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        print("start")
        urllib3.disable_warnings()
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self) -> None:
        time.sleep(1)
        print("end!")

    def test_002_LoginJenkins(self):
        print('运行第二条用例，登录jenkins')
        url = 'http://localhost:8080/jenkins/j_acegi_security_check'
        body={'j_username': 'wangyangyang',
'j_password': 'jiale8897',
'from':'',
'Submit': '登录',
'remember_me': 'on'}
        res=s.post(url,data=body)
        result=re.findall(u'<b>(.*?)</b></a>',res.text)[1]
        hope='注销'
        self.assertEqual(result,hope,msg='断言失败，请检查预期和实际结果！')


if __name__ == '__main__':
    unittest.main()
