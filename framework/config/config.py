# -*- coding: utf-8 -*-

'''
2017-03-09
webdriver全局获取
'''

__author__="liuf"
import sys
import getopt
import logging
import os
import time
import platform
from appium import webdriver

class Config(object):
    __PLATFORMiOS='iOS'
    __PLATFORMAndroid='Android'
    #iOS默认的bundle id
    __APPiOS='com.cditv.chengwang' #com.tencent.xin
    #android默认的包名
    __AppAndroid=''
    __deviceId=None
    __app=None
    #默认为iOS平台
    __platformName=None
    __report=None
    '''
    获取脚本执行时带入的参数
    '''
    @staticmethod
    def initShellArgv():
        # 获取传参内容，-r 测试报告的路径,-a 应用包的安装路径 -u 设备的udid
        # 短格式为-r,-a,-u,-p,-h，长格式为--report,--app,--udid,--platform,--help
        # 例如 python run.py  -r /Users/liuf/.jenkins/workspace/appiumTest/builds/20/appiumTest_20_report.html -a /Users/liuf/.jenkins/workspace/appiumTest/builds/20/appiumTest_20.ipa -u e5661d7c27872a52fc9df58577fcb81c41b88ed6 -p iOS
        opts, args = getopt.getopt(sys.argv[1:], 'r:a:u:p:h', ["report=", "app=", "udid=", "platform=", "help"])
        for opt, value in opts:
            if opt in ("-r", "--report"):
                Config.__report=value
            if opt in ("-a", "--app"):
                Config.__app=value
            if opt in ("-u", "--udid"):
                Config.__deviceId=value
            if opt in ("-p", "--platform"):
                Config.__platformName=value
            if opt in ("-h", "--help"):
                help()
    '''
    获取测试报告路径
    '''
    @staticmethod
    def getReport():
        if Config.__report==None:
            # 设置测试报告输出路径
            timestr=time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
            currentPath = os.getcwdu()
            separator = None
            if 'Windows' in platform.system():
                separator = '\\'
            else:
                separator = '/'
            Config.__report=currentPath+separator+'report'+separator+timestr+'.html'
        logging.info('测试包报告路径:%s' % Config.__report)
        return Config.__report
    '''
    获取平台类型
    '''
    @staticmethod
    def getPlatform():
        if Config.__platformName==Config.__PLATFORMiOS:
            logging.info('当前测试平台为:%s' % Config.__PLATFORMiOS)
            return Config.__PLATFORMiOS
        if Config.__platformName==Config.__PLATFORMAndroid:
            logging.info('当前测试平台为:%s' % Config.__PLATFORMAndroid)
            return Config.__PLATFORMAndroid
        logging.info('未指定测试平台默认为:%s' % Config.__PLATFORMiOS)
        return Config.__PLATFORMiOS
    '''
    获取设备id
    '''
    @staticmethod
    def getDeviceId():
        if Config.__deviceId!=None:
            logging.info('测试设备id:%s' % Config.__deviceId)
        return Config.__deviceId
    '''
    获取app路径
    '''
    @staticmethod
    def getAPP():
        if Config.__app==None:
            if Config.getPlatform()==Config.__PLATFORMiOS:
                logging.info('未指定app安装路径,通过iOS bundle id:%s启动应用' % Config.__APPiOS)
                return Config.__APPiOS
            else:
                logging.info('未指定app安装路径,通过android包名:%s启动应用' % Config.__AppAndroid)
                return Config.__AppAndroid
        else:
            logging.info('app安装路径:%s' % Config.__app)
            return Config.__app
    '''
    是否iOS测试平台
    '''
    @staticmethod
    def isiOSPlatform():
        if Config.getPlatform() == Config.__PLATFORMiOS:
            return True
        else:
            return False

    '''
    是否android测试平台
    '''
    @staticmethod
    def isAndroidPlatform():
        if Config.getPlatform() == Config.__PLATFORMAndroid:
            return True
        else:
            return False
