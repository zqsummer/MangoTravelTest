# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from commom.common import Common
from commom.my_error import MyError
from commom.my_logging import Logging
from page_actions.action_public import ActionPublic
from page_elements.element_cruiseShip import ElementCruiseShip
from page_elements.element_page_home import ElementPageHome
from page_elements.element_public import ElementPublic


class ActionCruiseShip:
    global result
    global action_public
    action_public = ActionPublic()
    global com
    com = Common()
    my_error = MyError()
    log = Logging()
    class_name = "ActionCruiseShip"

    def check_screen_factors(self,driver): #检查筛选因因子以及小红点
        try:
            function_name = "check_screen_factors"
            self.log.logStep(self.class_name + " - " + function_name)
            # self.log.logStep("进入app")
            # action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_HOME_SEARCH).click()  # 邮轮页 搜索按钮
            self.log.logStep("点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_SEARCH).click()  # 点击邮轮搜索
            if com.is_element_exist(driver,By.ID,ElementCruiseShip.ID_SCREEN_LIST):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_TRAVEL_DAY).click()  # 点击游玩天数
            self.log.logStep("选择最后一个天数")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH, value=ElementCruiseShip.XPATH_CHOSE_LASTDAY).click()  #游玩15天以上

            text = "15天以上"
            ActionCruiseShip.result = (text in driver.find_element(by=By.ID,value=ElementCruiseShip.ID_CHOOSEN_FACTOR).get_attribute('text')) \
                                      and com.is_element_exist(driver,By.ID,ElementCruiseShip.ID_RED_POINT)
            return  ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + str(e))
            self.my_error.error_catch(e, driver)
            return False

    def cruise_to_home(self,driver):#邮轮返回到首页
        try:
            function_name = "cruise_to_home"
            self.log.logStep(self.class_name + " - " + function_name)
            # self.log.logStep("进入app")
            # action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_HOME_SEARCH).click()  # 邮轮页 搜索按钮
            self.log.logStep("点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_SEARCH).click()  # 点击邮轮搜索
            self.log.logStep("点击返回首页")
            if com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_BACK_HOME):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_BACK_HOME).click()
            ActionCruiseShip.result = com.is_element_exist(driver,By.ID,ElementPageHome.ID_CRUISESHIP)
            return  ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + e.message)
            self.my_error.error_catch(e, driver)
            return False

    def clear_brand(self,driver): #筛选 选择邮轮品牌之后清除选项
        try:
            function_name = "clear_brand"
            self.log.logStep(self.class_name + " - " + function_name)
            # self.log.logStep("进入app")
            # action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_HOME_SEARCH).click()  # 邮轮页 搜索按钮
            self.log.logStep("点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_SEARCH).click()  # 点击邮轮搜索
            self.log.logStep("点击筛选")
            # if action_public.wait_page_loading(driver):
            if com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_SCREENING):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SCREENING).click()
            self.log.logStep("选择第一个邮轮品牌")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH, value=ElementCruiseShip.XPATH_SCREEN_BRAND).click()
            select_result = com.is_element_exist(driver,By.XPATH,ElementCruiseShip.XPATH_SELECT_IMG)
            self.log.logStep("点击清除选项")
            driver.find_element(by=By.ID,value=ElementCruiseShip.ID_CLEAR).click()
            clear_result = com.is_element_exist(driver,By.XPATH,ElementCruiseShip.XPATH_CLEAR_IMG)

            ActionCruiseShip.result = select_result and clear_result
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + str(e))
            self.my_error.error_catch(e, driver)
            return False

    def chose_brand(self,driver): #筛选  选择邮轮品牌
        try:
            function_name = "chose_brand"
            self.log.logStep(self.class_name + " - " + function_name)
            # self.log.logStep("进入app")
            # action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_HOME_SEARCH).click()  # 邮轮页 搜索按钮
            self.log.logStep("点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_SEARCH).click()  # 点击邮轮搜索
            self.log.logStep("点击筛选")
            # if action_public.wait_page_loading(driver):
            if com.is_element_exist(driver,By.ID,ElementCruiseShip.ID_SCREENING):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_SCREENING).click()
            self.log.logStep("选择第一个邮轮品牌")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_SCREEN_BRAND).click()
            self.log.logStep("点击确认")
            time.sleep(2)
            driver.find_element(by=By.ID,value=ElementCruiseShip.ID_SURE).click()#确认
            # driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_SURE)#确认
            text = "皇家加勒比邮轮"
            ActionCruiseShip.result = (text in driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_BRAND_FIRST).get_attribute('text'))
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + str(e))
            self.my_error.error_catch(e, driver)
            return False

    def chose_tralve_days(self,driver):
        try:
            function_name = "chose_tralve_days"
            self.log.logStep(self.class_name + " - " + function_name)
            # self.log.logStep("进入app")
            # action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_HOME_SEARCH).click()  # 邮轮页 搜索按钮
            self.log.logStep("点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_SEARCH).click()  # 点击邮轮搜索
            self.log.logStep("点击游玩天数")
            if com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_TRAVEL_DAY):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_TRAVEL_DAY).click() #点击游玩天数
            self.log.logStep("选择最后一个天数")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_CHOSE_LASTDAY).click() #
            ActionCruiseShip.result = com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_LIST_LINE) \
                                      or com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_NO_DATA)  # 有航线列表 或者 暂无内容
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + str(e))
            self.my_error.error_catch(e, driver)
            return False

    def sort_price(self,driver):#航线列表 价格排序
        try:
            function_name = "sort_price"
            self.log.logStep(self.class_name + " - " + function_name)
            # self.log.logStep("进入app")
            # action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_HOME_SEARCH).click()  # 邮轮页 搜索按钮
            self.log.logStep("点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_SHIP_SEARCH).click()  # 点击邮轮搜索
            self.log.logStep("点击价格排序")
            if com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_PRICE_SORT):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_PRICE_SORT).click() # 点击价格排序
            if com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_LIST_LINE):
                time.sleep(3)
                self.log.logStep("获取航线列表第一个价格")
                temp_str1 = driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_PRICE_FIRST).get_attribute('text')
                self.log.logStep("获取航线列表第二个价格")
                temp_str2 = driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_PRICE_SECOND).get_attribute('text')
                ActionCruiseShip.result = temp_str1<=temp_str2
                return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + str(e))
            self.my_error.error_catch(e, driver)
            return False

    def mango_recomend(self,driver): #航线列表芒果推荐
        try:
            function_name = "mango_recomend"
            self.log.logStep(self.class_name + " - " + function_name)
            # self.log.logStep("进入app")
            # action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_HOME_SEARCH).click()  # 邮轮页 搜索按钮
            self.log.logStep("点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_SEARCH).click()  # 点击邮轮搜索
            self.log.logStep("点击邮轮推荐")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_RECOMMEND).click() #点击芒果推荐

            ActionCruiseShip.result = com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_LIST_LINE) \
                                      or com.is_element_exist(driver,By.ID,ElementCruiseShip.ID_NO_DATA) #有航线列表 或者 暂无内容
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + str(e))
            self.my_error.error_catch(e, driver)
            return False

    def search_cruiseShip(self, driver): #查询邮轮
        try:
            function_name = "search_cruiseShip"
            self.log.logStep(self.class_name+" - " + function_name +" - 进入app")
            action_public.enter_app(driver)
            self.log.logStep(self.class_name + " - " + function_name +" - home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep(self.class_name + " - " + function_name + " - 邮轮主页点击搜索图标")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_HOME_SEARCH).click() #邮轮页 搜索按钮
            self.log.logStep(self.class_name + " - " + function_name + " - 邮轮航线选择")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_LINE).click() #邮轮航线选择
            self.log.logStep(self.class_name + " - " + function_name + " - 选择第一个航线")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH, value=ElementCruiseShip.XPATH_FIRST_LINE).click()#选择第一个航线
            self.log.logStep(self.class_name + " - " + function_name + " - 点击出发港口")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_PORT).click()# 出发港口
            self.log.logStep(self.class_name + " - " + function_name + " - 选择第一个港口")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH, value=ElementCruiseShip.XPATH_FIRST_PORT).click()#选择第一个港口
            self.log.logStep(self.class_name + " - " + function_name + " - 点击邮轮搜索")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_SHIP_SEARCH).click()#点击邮轮搜索
            # Common.pass_condition = "元素-航线列表"
            ActionCruiseShip.result = com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_LIST_LINE) #搜索出来的航线列表
            return ActionCruiseShip.result
        except Exception as e:
            print e.message
            self.my_error.error_catch(e, driver)
            return False

    def into_cruiseBK(self, driver): #进入邮轮百科
        try:
            function_name = "into_cruiseBK"
            # self.log.logStep(self.class_name + " - " + function_name + " - 进入app")
            # action_public.enter_app(driver)
            self.log.logStep(self.class_name + " - " + function_name + " - home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep(self.class_name + " - " + function_name + " - 点击邮轮百科")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_CRUISE_BK).click() #点击邮轮百科
            Common.pass_condition = "元素-邮轮自述图片"
            # ActionCruiseShip.result = com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_PIC_OF_CRUISE_BK)#邮轮百科的图片是否加载出来
            # Common.pass_condition = "文本-邮轮百科"
            ActionCruiseShip.result = com.is_text_exist(driver,"邮轮百科")
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep(self.class_name + " - " + function_name + " - Exception : " + e.message)
            self.my_error.error_catch(e, driver)
            return False

    def order_bargain_cruise(self, driver):
        '''订购特价限时抢购'''
        try:
            function_name = "order_bargain_cruise"
            self.log.logStep(self.class_name + " - " + function_name + " - 进入app")
            action_public.enter_app(driver)
            self.log.logStep(self.class_name + " - " + function_name + " - home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep(self.class_name + " - " + function_name + " - 特价限时抢购")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_BARGAIN).click()#特价限时抢购
            self.log.logStep(self.class_name + " - " + function_name + " - 更多航期")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_MORE_DATE).click() #更多航期
            self.log.logStep(self.class_name + " - " + function_name + " - 选择最后一个航期")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH, value=ElementCruiseShip.XPATH_LAST_DATE).click() #选择最后一个航期
            self.log.logStep(self.class_name + " - " + function_name + " - 选择第一个预订")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.XPATH, value=ElementCruiseShip.XPATH_FIRST_RESERVE).click()#选择第一个预订
            if com.is_element_exist(driver, By.ID, ElementPublic.ID_LOGIN_NUME): #如果不是填写订单页面，即是登录账号页面
                self.log.logStep(self.class_name + " - " + function_name + " - 登录账号页面")
                action_public.login(driver) #输入用户名密码登录
            self.log.logStep(self.class_name + " - " + function_name + " - 填写订单，用户名+测试")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementCruiseShip.ID_ORDER_USERNAME).send_keys(u"钟琴测试")
            self.log.logStep(self.class_name + " - " + function_name + " - 提交订单")
            driver.find_element(by=By.ID, value=ElementCruiseShip.ID_ORDER_SUBMIT).click()#提交订单  慎用

            text = "订单提交成功"
            # ActionCruiseShip.result = Common.is_text_exist(text)
            ActionCruiseShip.result = (text in driver.find_element(by=By.ID, value=ElementCruiseShip.ID_ORDER_SUCESS).get_attribute("text"))
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep(self.class_name + " - " + function_name + " - Exception : ",e)
            self.my_error.error_catch(e, driver)
            return False

    def into_cruiseBC(self,driver):#进入邮轮包船
        try:
            function_name = "into_cruiseBC"
            self.log.logStep(self.class_name + " - " + function_name)
            self.log.logStep("进入app")
            action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("点击邮轮包船")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID,value=ElementCruiseShip.ID_BAOCHUAN).click()

            ActionCruiseShip.result = com.is_element_exist(driver, By.ID, ElementCruiseShip.ID_PIC_OF_BAOCHUAN)  # 邮轮包船的图片是否加载出来
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : "+ str(e))
            self.my_error.error_catch(e, driver)
            return False

    def check_crusie_home(self,driver): #检查邮轮首页
        try:
            function_name = "check_crusie_home"
            self.log.logStep(self.class_name + " - " + function_name)
            self.log.logStep("进入app")
            action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")
            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()

            ActionCruiseShip.result= com.is_element_exist(driver,By.ID,ElementCruiseShip.ID_TOPAD)#邮轮首页顶部广告
            return ActionCruiseShip.result
        except Exception as e:
            self.log.logStep("Exception : " + e)
            self.my_error.error_catch(e, driver)
            return False

    def check_area_product(self,driver): #检查各地域推荐产品
        try:
            function_name = "check_area_product"
            self.log.logStep(self.class_name + " - " + function_name)
            self.log.logStep("进入app")
            action_public.enter_app(driver)
            self.log.logStep("home主页点击邮轮")

            if action_public.wait_page_loading(driver):
                driver.find_element(by=By.ID, value=ElementPageHome.ID_CRUISESHIP).click()
            self.log.logStep("滑动到推荐产品")
            if action_public.wait_page_loading(driver):
                driver.swipe(850,1500,900,700)

            self.log.logStep( "点击东南亚")
            driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_DNY).click()
            self.log.logStep("点击地中海")
            driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_DZH).click()
            self.log.logStep("点击阿拉斯加")
            driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_ALSJ).click()
            self.log.logStep("点击日韩")
            driver.find_element(by=By.XPATH,value=ElementCruiseShip.XPATH_RH).click()
            self.log.logStep("点击进入详情")
            driver.find_element(by=By.ID,value=ElementCruiseShip.ID_AREA_FIRST).click()#点击进入详情

            ActionCruiseShip.result = com.is_element_exist(driver,By.ID,ElementCruiseShip.ID_CRUISE_TITLE)
            return ActionCruiseShip.result
        except Exception as e:
            # print type(e.message)
            # self.log.logStep(type(e.message))
            self.log.logStep("Exception : "+str(e))
            self.my_error.error_catch(e, driver)
            return False































