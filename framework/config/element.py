# -*- coding: utf-8 -*-

'''
2017-03-09
获取配置文件中的element
'''

__author__="liuf"

import os
import glob
import platform
import logging
import xml.dom.minidom
from config import Config
import common.driver
class Element(object):
    __elements=[]

    '''
    获取当前目录下的所有配置文件并加载到内存中，因为是单机程序故使用DOM方式加载
    '''
    @staticmethod
    def loadElements():
        currentPath=os.getcwdu()
        separator=None
        if 'Windows' in platform.system():
            separator='\\'
        else:
            separator='/'
        files=glob.glob(currentPath+separator+'xml'+separator+'*.xml')
        for file in files:
            #打开xml文件
            dom=xml.dom.minidom.parse(file)
            #得到所有的element元素
            Element.__elements.extend(dom.documentElement.getElementsByTagName('element'))
    '''
    根据测试平台类型（ios或者android）获取指定名称的元素，如果配置多种查找方式则优先级为xpath>>name>>class
    '''
    @staticmethod
    def getElement(key,classFilter=None,nameFilter=None):
        child=Element.__getChildElement(key)
        if child!=None:
            if len(child.getElementsByTagName('xpath')) > 0:
                xpathElement = child.getElementsByTagName('xpath')[0]
                try:
                    return common.driver.Driver.getDriver().find_element_by_xpath(xpathElement.firstChild.data)
                except BaseException as e:
                    logging.info('通过xpath方式未找到%s指定的元素' % key)
            elif len(child.getElementsByTagName('name')) > 0:
                nameElement = child.getElementsByTagName('name')[0]
                els=common.driver.Driver.getDriver().find_elements_by_name(nameElement.firstChild.data)
                if len(els)>0:
                    if classFilter!=None:
                        for el in els:
                            if el.tag_name==classFilter:
                                return el
                    else:
                        #取第一个
                        return els[0]
                else:
                    logging.info('通过name方式未找到%s指定的元素' % key)
            elif len(child.getElementsByTagName('class')) > 0:
                classElement = child.getElementsByTagName('class')[0]
                els=common.driver.Driver.getDriver().find_elements_by_class_name(classElement.firstChild.data)
                if len(els)>0:
                    if nameFilter!=None:
                        for el in els:
                            if el.name==nameFilter:
                                return el
                    else:
                        #取第一个
                        return els[0]
                else:
                    logging.info('通过clsss方式未找到%s指定的元素' % key)
        return None

    '''
    指定通过xpath方式获取元素
    '''
    @staticmethod
    def getElementWithXpath(key):
        child=Element.__getChildElement(key)
        if child!=None:
            if len(child.getElementsByTagName('xpath')) > 0:
                xpathElement = child.getElementsByTagName('xpath')[0]
                try:
                    return common.driver.Driver.getDriver().find_element_by_xpath(xpathElement.firstChild.data)
                except BaseException as e:
                    logging.info('通过xpath方式未找到%s指定的元素' % key)
        return None
    '''
    指定通过name方式获取元素
    '''
    @staticmethod
    def getElementWithName(key,classFilter=None):
        child=Element.__getChildElement(key)
        if child!=None:
            if len(child.getElementsByTagName('name')) > 0:
                nameElement = child.getElementsByTagName('name')[0]
                els=common.driver.Driver.getDriver().find_elements_by_name(nameElement.firstChild.data)
                if len(els)>0:
                    if classFilter!=None:
                        for el in els:
                            if el.tag_name==classFilter:
                                return el
                    else:
                        #取第一个
                        return els[0]
                else:
                    logging.info('通过name方式未找到%s指定的元素' % key)
        return None
    '''
    指定通过class方式获取元素
    '''
    @staticmethod
    def getElementWithClass(key,nameFilter=None):
        child=Element.__getChildElement(key)
        if child!=None:
            if len(child.getElementsByTagName('class')) > 0:
                classElement = child.getElementsByTagName('class')[0]
                els=common.driver.Driver.getDriver().find_elements_by_class_name(classElement.firstChild.data)
                if len(els)>0:
                    if nameFilter!=None:
                        for el in els:
                            if el.name==nameFilter:
                                return el
                    else:
                        #取第一个
                        return els[0]
                else:
                    logging.info('通过clsss方式未找到%s指定的元素' % key)
        return None
    '''
    获取子元素
    '''
    @staticmethod
    def __getChildElement(key):
        element=None
        for el in Element.__elements:
            if el.getAttribute('key')==key:
                element=el
                break
        if element!=None:
            child=None
            if len(element.getElementsByTagName('general')) > 0:
                child=element.getElementsByTagName('general')[0]
            elif len(element.getElementsByTagName('iOS')) > 0 and Config.isiOSPlatform():
                child=element.getElementsByTagName('ios')[0]
            elif len(element.getElementsByTagName('android')) > 0 and Config.isAndroidPlatform():
                child=element.getElementsByTagName('android')[0]
            return child
        return None