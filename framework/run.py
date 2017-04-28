# -*- coding: utf-8 -*-

'''
2017-03-09
整个测试脚本的启动类
'''

__author__="liuf"
import getopt
import logging
import sys
import unittest
from common import *
from usercenter_testcase import *
from config import *
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # 设置系统默认编码
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # 获取脚本执行时的参数
    Config.initShellArgv()
    # 加载元素配置文件
    Element.loadElements()
    # 初始化webdriver
    driver=Driver.getDriver()
    if driver!=None:
        #使用测试报告模板
        fp = open(Config.getReport(), 'wb')
        runner=HTMLTestRunner(
            stream=fp,
            title='result',
            description='report'
        )
        # 加载测试用例
        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LoginCase))
        runner.run(suite)
        fp.close()
    else:
        logging.info('---------启动测试失败！---------')