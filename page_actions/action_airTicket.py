# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from commom.common import Common
from commom.my_error import MyError
from page_actions.action_public import ActionPublic
from page_elements.element_airTicket import ElementAirTicket
from page_elements.element_city_choose import ElementCity
from page_elements.element_page_home import ElementPageHome


class ActionAirTicket:
    global result
    global action_public
    action_public=ActionPublic()
    global com
    com = Common()
    my_error=MyError()

    #查询机票
    def search_ticket(self,driver,start_city,to_city):
        try:
            action_public.enter_app(driver)
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_FLIGHT).click()
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementAirTicket.ID_START_CITY).click()#默认的出发城市测试改错了 记得改回来
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementCity.ID_BANK_SEARCH).send_keys(start_city) # #城市输入框 输入出发城市
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementCity.ID_CITY_CHOOSEN).click() #搜索出来的城市选择
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementAirTicket.ID_TO_CITY).click() #默认的到达城市
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCity.ID_BANK_SEARCH).send_keys(to_city) # 输入到达城市
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCity.ID_CITY_CHOOSEN).click()#搜索出来的城市选择
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementAirTicket.ID_SEARCH).click() #点击查询

            text = start_city+"-"+to_city
            # Common.pass_condition = "文本-"+text
            ActionAirTicket.result = com.is_text_exist(driver,text)
            return ActionAirTicket.result
        except Exception as e:
            print e.message
            self.my_error.error_catch(e,driver)
            return False



if __name__ == "__main__":
    com = Common()
    com.start_appium()
    com.setUp_appium()
    driver = com.driver
    aat = ActionAirTicket()
    sleep(3)
    result=aat.search_ticket(driver,"shanghai","shenzhen")
    print "result : ",result








