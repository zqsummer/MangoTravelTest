# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By

from commom.common import Common
from page_elements.element_public import ElementPublic


class  ActionPublic:
    global com
    com = Common()

    def login(self,driver,username=com.loginUsername,passward=com.loginPwd):
        '''提交订单页面  登录'''
        driver.find_element(by=By.ID,value=ElementPublic.ID_LOGIN_NUME).send_keys(username) #登陆账号
        driver.find_element(by=By.ID,value=ElementPublic.ID_PWD).send_keys(passward)#登录密码
        driver.find_element(by=By.ID,value=ElementPublic.ID_LOGIN_BTN).click() #登录按钮
        time.sleep(3)

    def wait_page_loading(self,driver):
        '''等待页面加载完成  即小黄人消失'''
        count = 0
        while (com.wait_element(driver,By.ID, ElementPublic.ID_LOADING)):
            time.sleep(1)
            count+=1
            if (count > 15): # 15秒超时
                return False
        return True

    def enter_app(self,driver):
        '''安装app 开始时候点击立即体检进入'''
        driver.swipe(900, 900, 100, 900)
        driver.swipe(900, 900, 100, 900)
        driver.find_element(by=By.ID, value=ElementPublic.ID_ENTER).click()
        time.sleep(3)

