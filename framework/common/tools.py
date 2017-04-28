# -*- coding: utf-8 -*-

'''
2017-03-09
工具类
'''
__author__="liuf"

from driver import Driver
from time import sleep
import random
import string
import os
import tempfile
import logging
class Tools(object):
    TOOLS_HOME='首页'
    '''
    返回到主界面
    '''
    @staticmethod
    def goMainPage():
        driver=Driver.getDriver()
        homes=driver.find_elements_by_name(Tools.TOOLS_HOME)
        if len(homes)>0:
            return
        else:
            backBtn=driver.find_elements_by_name('back btn normal t')
            if len(backBtn)>0:
                backBtn[0].click()
            backBtn=driver.find_elements_by_name('video_btn_fanhui_normal.png')
            if len(backBtn)>0:
                backBtn[0].click()
            backBtn=driver.find_elements_by_name('login_btn_quxiao_normal.png')
            if len(backBtn)>0:
                backBtn[0].click()
            Tools.sleep()
            Tools.goMainPage()
    '''
    是否在主页
    '''
    @staticmethod
    def isMainPage():
        homes=Driver.getDriver().find_elements_by_name(Tools.TOOLS_HOME)
        if len(homes)>0:
            return True
        else:
            return False
    '''
    统一的sleep方法
    '''
    @staticmethod
    def sleep(t=0.5):
        sleep(t)
    '''
    获得机器屏幕大小x,y
    '''
    @staticmethod
    def getSize():
        x = Driver.getDriver().get_window_size()['width']
        y = Driver.getDriver().get_window_size()['height']
        return (x, y)

    '''
    屏幕向上滑动
    '''
    @staticmethod
    def swipeUp(t):
        l = Tools.getSize()
        x = int(l[0] * 0.5)
        y = int(l[1] * 0.5)
        Driver.getDriver().swipe(x, y, 0, -100, t)

    '''
    屏幕向下滑动
    '''
    @staticmethod
    def swipeDown(t):
        l = Tools.getSize()
        x = int(l[0] * 0.5)
        y = int(l[1] * 0.5)
        Driver.getDriver().swipe(x, y, 0, 100, t)

    '''
    屏幕向左滑动
    '''
    @staticmethod
    def swipLeft(t):
        l = Tools.getSize()
        x = int(l[0] * 0.5)
        y = int(l[1] * 0.5)
        Driver.getDriver().swipe(x, y, -100, 0, t)

    '''
    屏幕向右滑动
    '''
    @staticmethod
    def swipRight(t):
        l = Tools.getSize()
        x = int(l[0] * 0.5)
        y = int(l[1] * 0.5)
        Driver.getDriver().swipe(x, y, 100, 0, t)
    '''
    获取指定位数的随机字母和数字
    '''
    @staticmethod
    def random(size=4):
        list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        return ''.join(random.sample(list,size))

