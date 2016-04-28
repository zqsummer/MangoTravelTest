# -*- coding: utf-8 -*-
import time
import unittest

from commom.my_send import SendMail
from testcases.cases_airTicket import CasesAirTicket
from testcases.cases_cruiseShip import CasesCruiseShip


class tests_all:

        print "start to test all the cases...."
        suit = unittest.TestSuite()
        # suit.addTest(cases_airTicket("test_search_ticket"))
        suit.addTest(unittest.makeSuite(CasesAirTicket))
        suit.addTest(unittest.makeSuite(CasesCruiseShip))
        #
        # #执行测试
        runner = unittest.TextTestRunner()
        runner.run(suit)
        ##生成测试报告
        # cur_date = time.strftime("%Y%m%d%H%M%S")
        # report_path = "../results/testResult_" + cur_date + ".html"
        # # report_path = "ftp:/10.10.152.9/testResult_"+cur_date+".html"
        # fp = file(report_path, 'wb')
        # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
        # runner.run(suit)
        print "all the cases done"
        #发送测试报告邮件
        print "准备发送测试报告邮件。。。"
        time.sleep(3)
        mysend = SendMail()
        ret_cruseShip = mysend.parse_lis(CasesCruiseShip.lis_cruiseShip)
        ret_airTicket = mysend.parse_lis(CasesAirTicket.lis_airTicket)
        all_list = [ret_cruseShip, ret_airTicket]
        # all_list = [ret_airTicket]
        mysend.sen_mail(all_list)
        print "the end"



