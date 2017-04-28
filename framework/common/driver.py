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
from appium import  webdriver
from config import Config

class Driver(object):
    __driver=None
    '''
    测试初始化设置
    '''
    @staticmethod
    def getDriver():
        if Driver.__driver==None:
            logging.info('---------初始化webdriver开始---------')
            Driver.__driver = None
            # 没有指定设备则从连接到系统的设备中选取一个
            if Config.getDeviceId() == None:
                # 执行shell获取当前系统连接的设备的udid
                udids = os.popen('system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "##').read().split()
                if len(udids) > 0:
                    logging.info('未指定测试设备，从当前连接设备中选取:%s' % udids[0])
                    Driver.__driver = webdriver.Remote(
                        command_executor='http://10.100.131.110:4723/wd/hub',
                        desired_capabilities={
                            'app': Config.getAPP(),
                            'platformName': Config.getPlatform(),
                            'platformVersion': '9.3',
                            'deviceName': 'iphone 5',
                            'udid': udids[0]
                        }
                    )
                else:
                    logging.info('---------未检测到测试设备---------')
            else:
                Driver.__driver = webdriver.Remote(
                    command_executor='http://10.100.131.110:4723/wd/hub',
                    desired_capabilities={
                        'app': Config.getAPP(),
                        'platformName': Config.getPlatform(),
                        'platformVersion': '9.3',
                        'deviceName': 'iphone 5',
                        'udid': Config.getDeviceId()
                    }
                )
            if Driver.__driver==None:
                logging.info('---------webdriver初始化失败---------')
            return Driver.__driver
        else:
            return Driver.__driver

