# -*- coding: utf-8 -*-

'''
2017-03-09
登陆测试用例
'''

__author__="liuf"
import logging
import unittest
from time import sleep
from common import *
from config import Element

class LoginCase(unittest.TestCase):
    '''
    测试开始进入用户中心界面
    '''
    def setUp(self):
        if Tools.isMainPage()!=True:
            Tools.goMainPage()
        item=Element.getElement('main.bottom.bar.uc')
        if item!=None:
            item.click()
            Tools.sleep()

    '''
    测试完成后回到主界面
    '''
    def tearDown(self):
        if Tools.isMainPage()!=True:
            Tools.goMainPage()
    '''
    账号登陆测试用例
    '''
    def test_login(self):
        self.__logout()
        logging.info('---------测试登陆开始---------')
        goLoginBtn=Element.getElement('uc.mainpage.loginlink')
        goLoginBtn.click()
        Tools.sleep()
        # 获取账号输入框
        usernameTextField=Element.getElement('uc.loginpage.username')
        # 获取密码输入框
        passwordTextField=Element.getElement('uc.loginpage.password')
        # 输入待测试账号密码
        usernameTextField.clear()
        usernameTextField.send_keys('18628331478')
        passwordTextField.clear()
        passwordTextField.send_keys('123456')
        loginBtn=Element.getElement('uc.loginpage.loginbtn',classFilter='XCUIElementTypeButton')
        loginBtn.click()
        Tools.sleep()
        self.assertTrue(self.__findIsLogin())
        logging.info('---------测试登陆结束---------')
    '''
    注销测试用例
    '''
    def test_logout(self):
        self.__logout()
        self.assertFalse(self.__findIsLogin())
    '''
    注销
    '''
    def __logout(self):
        if self.__findIsLogin():
            logging.info('---------注销登陆开始---------')
            #点击用户信息按钮
            userInfoBtn=Element.getElement('uc.mainpage.userinfolink')
            userInfoBtn.click()
            Tools.sleep()
            #滚动列表
            Tools.swipeUp(100)
            logoutCell=Element.getElement('uc.userinfopage.logoutbtn')
            logoutCell.click()
            Tools.sleep()
            logging.info('---------注销登陆结束---------')
    '''
    查询是否登陆
    '''
    def __findIsLogin(self):
        isLogin=Element.getElement('uc.mainpage.loginflag')
        if isLogin!=None:
            return False
        else:
            return True
    '''
    获取登陆验证码
    '''
    def __getCheckCode(self):
        codeImage=None
        try:
            codeImage = Driver.getDriver().find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeImage[2]')
        except BaseException as e:
            logging.info('---------登陆验证码不存在---------')
        return codeImage