# -*- coding:utf-8 -*-
# @Time:  2020/1/3 11:25
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  test_03.py
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

    def test_003_GetJenkins(self):
        print('运行第三条用例，提交任务')
        url = 'http://localhost:8080/jenkins/j_acegi_security_check'
        body = {'j_username': 'wangyangyang',
                'j_password': 'jiale8897',
                'from': '',
                'Submit': '登录',
                'remember_me': 'on'}
        res1 = s.post(url, data=body)
        url2 = 'http://localhost:8080/jenkins/user/wangyangyang/my-views/view/all/createItem'
        body2={'name': 1000,
'mode': 'hudson.maven.MavenModuleSet',
'from':'',
'Jenkins-Crumb': 'd4052370eacecaed11f21e457a931612',
'json': '{"name": "1000", "mode": "hudson.maven.MavenModuleSet", "from": "", "Jenkins-Crumb": "d4052370eacecaed11f21e457a931612"}'}
        res=s.post(url2,data=body2)
        print(res.text)
        # result=re.findall(u'"section-header">(.*?)</div></td>',res.text)[1]
        # hope='构建触发器'
        # self.assertEqual(result,hope)


if __name__ == '__main__':
    unittest.main()
