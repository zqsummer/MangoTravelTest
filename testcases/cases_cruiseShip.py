# -*- coding: utf-8 -*-
import HTMLTestRunner
import time
import unittest

from commom import my_send
from commom.common import Common
from commom.my_appium import MyAppium
from commom.my_logging import Logging
from page_actions.action_cruiseShip import ActionCruiseShip
from testcases.cases_airTicket import CasesAirTicket


class CasesCruiseShip(unittest.TestCase):
    global test_case_name
    global result
    moudle_name = "邮轮"
    moudle_Id = "002"
    lis_cruiseShip=[]
    global action_cruiseShip
    global my_log
    action_cruiseShip = ActionCruiseShip()
    my_log=Logging()
    my_appium = MyAppium()

    def setUp(self):
        self.my_appium.start_appium()
        self.driver = self.my_appium.setUp_appium()

    def tearDown(self):
        #强制关闭
        self.my_appium.take_cmd("taskkill /f /im node.exe")

    def test_clear_brand(self):
        Common.test_case_Id = self.moudle_Id + "013"
        self.test_case_name = "航线列表-选择邮轮品牌后清除选项"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.clear_brand(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_check_screen_factors(self):
        Common.test_case_Id = self.moudle_Id + "012"
        self.test_case_name = "航线列表-筛选因子及小红点检查"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.check_screen_factors(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_cruise_to_home(self):
        Common.test_case_Id = self.moudle_Id + "011"
        self.test_case_name = "航线列表-返回首页"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.cruise_to_home(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_chose_brand(self):
        Common.test_case_Id = self.moudle_Id + "010"
        self.test_case_name = "航线列表-筛选"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.chose_brand(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_chose_tralve_days(self):
        Common.test_case_Id = self.moudle_Id + "009"
        self.test_case_name = "航线列表-游玩天数"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.chose_tralve_days(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_sort_price(self):
        Common.test_case_Id = self.moudle_Id+"008"
        self.test_case_name = "航线列表-价格排序"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.sort_price(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_mango_recomend(self):
        Common.test_case_Id = self.moudle_Id + "007"
        self.test_case_name = u"航线列表-芒果推荐"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.mango_recomend(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)


    def test_search_cruiseShip(self):
        Common.test_case_Id = self.moudle_Id + "006"
        self.test_case_name = "查询邮轮"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.search_cruiseShip(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name,Common.test_case_Id,Common.test_case_name,self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_into_curiseBK(self):
        Common.test_case_Id = self.moudle_Id + "005"
        self.test_case_name = "进入邮轮百科"
        Common.test_case_name = self.test_case_name

        self.result = action_cruiseShip.into_cruiseBK(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)

        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]  #[模块名称，用例id，用例名称，结果]
        self.lis_cruiseShip.append(lis)  #[[模块名称，用例id，用例名称，结果],[模块名称，用例id，用例名称，结果]......]
        self.assertTrue(self.result)

    def test_order_bargain_cruise(self): #特价限时抢购预订
        Common.test_case_Id = self.moudle_Id+"004"
        self.test_case_name = u"特价限时抢购预订"
        Common.test_case_name = self.test_case_name

        self.result=action_cruiseShip.order_bargain_cruise(self.driver)

        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)
        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_cruiseShip.append(lis)
        self.assertTrue(self.result)

    def test_into_cruiseBC(self):
        Common.test_case_Id = self.moudle_Id + "003"
        self.test_case_name = "进入邮轮包船"
        Common.test_case_name = self.test_case_name
        self.result = action_cruiseShip.into_cruiseBC(self.driver)#进入邮轮包船
        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)

        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]  # [模块名称，用例id，用例名称，结果]
        self.lis_cruiseShip.append(lis)  # [[模块名称，用例id，用例名称，结果],[模块名称，用例id，用例名称，结果]......]
        self.assertTrue(self.result)

    def test_check_crusie_home(self):
        Common.test_case_Id = self.moudle_Id + "002"
        self.test_case_name = u"检查邮轮首页"
        Common.test_case_name = self.test_case_name
        self.result = action_cruiseShip.check_crusie_home(self.driver) #检查邮轮首页banner大图
        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)

        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]  # [模块名称，用例id，用例名称，结果]
        self.lis_cruiseShip.append(lis)  # [[模块名称，用例id，用例名称，结果],[模块名称，用例id，用例名称，结果]......]
        self.assertTrue(self.result)

    def test_check_area_product(self):
        Common.test_case_Id = self.moudle_Id + "001"
        self.test_case_name = u"检查地域切换及推荐产品"
        Common.test_case_name = self.test_case_name
        self.result = action_cruiseShip.check_area_product(self.driver)  # 检查地域切换及推荐产品
        my_log.logger(Common.test_case_Id, self.moudle_name, Common.test_case_name, self.result)

        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]  # [模块名称，用例id，用例名称，结果]
        self.lis_cruiseShip.append(lis)  # [[模块名称，用例id，用例名称，结果],[模块名称，用例id，用例名称，结果]......]
        self.assertTrue(self.result)


if __name__ == "__main__":
    suit = unittest.TestSuite()
    # suit.addTest(cases_airTicket("test_search_ticket"))
    suit.addTest(unittest.makeSuite(CasesAirTicket))
    suit.addTest(unittest.makeSuite(CasesCruiseShip))

    # #执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
    cur_date = time.strftime("%Y%m%d%H%M%S")
    report_path = "../results/testResult_"+ cur_date + ".html"
    fp = file(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(suit)
    print "准备发送测试报告邮件"
    # 发送测试报告邮件
    mysend = my_send.SendMail()
    ret_cruseShip = mysend.parse_lis(CasesCruiseShip.lis_cruiseShip)
    # print "ret_cruseShip:",ret_cruseShip
    ret_airTicket = mysend.parse_lis(CasesAirTicket.lis_airTicket)
    # print "ret_airTicket:", ret_airTicket
    all_list = [ret_cruseShip, ret_airTicket]
    # print type(all_list),all_list
    # all_list = [ret_cruseShip]

    # to_list = "qin.zhong@mangocity.com"
    mysend.sen_mail(all_list)
    print "the end"
    #
