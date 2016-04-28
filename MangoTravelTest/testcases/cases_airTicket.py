# -*- coding: UTF-8 -*-
import unittest

from commom.common import Common
from commom.my_appium import MyAppium
from commom.my_logging import Logging
from page_actions.action_airTicket import ActionAirTicket


class CasesAirTicket(unittest.TestCase):
    global driver
    global test_case_name
    global result
    moudle_name = u"机票"
    moudle_Id = "001"
    lis_airTicket = []
    global my_log,action_airTicket
    my_log = Logging()
    my_appium = MyAppium()
    action_airTicket = ActionAirTicket()
    def setUp(self):
        self.my_appium.start_appium()
        self.driver = self.my_appium.setUp_appium()

    def tearDown(self):
        self.my_appium.quit_appium()

    def test_search_ticket(self):
        Common.test_case_Id = self.moudle_Id+"001"
        self.test_case_name = u"查询机票"
        Common.test_case_name = self.test_case_name

        self.result = action_airTicket.search_ticket(self.driver,u"上海",u"深圳")

        lis = [self.moudle_name, Common.test_case_Id, Common.test_case_name, self.result]
        self.lis_airTicket.append(lis)
        my_log.logger(Common.test_case_Id,self.moudle_name,Common.test_case_name,self.result)
        self.assertTrue(self.result)


if __name__ == "__main__":
    suit = unittest.TestSuite()
    # suit.addTest(cases_airTicket("test_search_ticket"))
    suit.addTest(unittest.makeSuite(CasesAirTicket))
    # suit.addTest(unittest.makeSuite(cases_cruiseShip))
    #
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suit)
    # import sys
    #
    # reload(sys)
    # sys.setdefaultencoding('utf-8')  # 这里是为解决生成报告中文编码问题
    # cur_date = time.strftime("%Y%m%d%H%M%S")
    # report_path = "../results/testResult_"+cur_date+".html"
    # # report_path = "ftp:/10.10.152.9/testResult_"+cur_date+".html"
    # fp = file(report_path, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    # runner.run(suit)

    # 发送测试报告邮件
    mysend = SendMail()
    # ret_cruseShip = mysend.parse_lis(cases_cruiseShip.lis_cruiseShip)
    # print "ret_cruseShip:",ret_cruseShip
    ret_airTicket = mysend.parse_lis(CasesAirTicket.lis_airTicket)
    # print "ret_airTicket:", ret_airTicket
    # all_list = [ret_cruseShip, ret_airTicket]
    # print type(all_list),all_list
    all_list = [ret_airTicket]
    print type(all_list), all_list
    # to_list = "qin.zhong@mangocity.com,tiezhu.liu@mangocity.com,hong.hao@mangocity.com"

    mysend.sen_mail(all_list)
    print "the end"










