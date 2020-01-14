# -*- coding:utf-8 -*-
# @Time:  2020/1/3 11:25
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  test_01.py
# @Software:  PyCharm

import requests
import unittest
import time
import re
import urllib3
import warnings
from loguru import logger
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
logger.add("E:\\honggetest\\log\\"+today+".log",encoding='utf8',retention='30 days')  # 日志打印到文件
# logger.add('E:\\honggetest\\log\\file_1.log',encoding='utf-8',rotation='500 MB')
# logger.add('E:\\honggetest\\log\\file_1.log',encoding='utf8',rotation='1 week')
# logger.add('E:\\honggetest\\log\\file_1.log',encoding='utf8',retention='10 days')
# logger.add('E:\\honggetest\\log\\file_1.log',encoding='utf8',compression='zip')
s=requests.session()


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        logger.debug("start")
        urllib3.disable_warnings()
        warnings.simplefilter("ignore",ResourceWarning)

    def tearDown(self) -> None:
        time.sleep(1)
        logger.debug("end!")

    def test_001_GetBaiDu(self):
        logger.info('运行第一条用例，获取百度首页')
        url="https://www.baidu.com"
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        res=s.get(url,headers=head,verify=False)
        res.encoding='utf-8'
        result=re.findall(u'<title>(.*?)，你就',res.text)[0]
        hope='百度一下'
        self.assertEqual(result,hope,msg='断言失败，请检查预期和实际结果！')
        logger.info('第一条用例执行结束！')


if __name__=='__main__':
    unittest.main()
