# -*- coding:utf-8 -*-
# @Time:  2020/1/3 14:22
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  run_all_case.py
# @Software:  PyCharm

import unittest


# 加载用例并使用套件组装
def all_case():
    dir='E:\\honggetest\\case'
    disvover=unittest.defaultTestLoader.discover(start_dir=dir,pattern='test*.py',top_level_dir=None)
    suite=unittest.TestSuite()
    suite.addTests(disvover)
    return suite


# 一次性运行并生成测试报告
if __name__=='__main__':
    import HTMLTestRunner
    import time
    now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
    report_path="E:\\honggetest\\report\\result "+now+".html"
    fb=open(report_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fb,title="这是我的报告",description="测试4个用例....",verbosity=2)
    runner.run(all_case())
    fb.close()