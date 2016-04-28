# -*- coding: utf-8 -*-
from commom.common import Common


class MyError:
    global com
    com  = Common()

    def error_catch(self, e, driver):
        '''处理各种异常'''
        # print "Exception : ",e
        # print u"进入异常处理"
        # # mail_to = "qin.zhong@mangocity.com"
        # #异常原因
        # Common.exception_essage = "其他异常原因"
        # if "An element could not be located" in str(e):
        #     Common.exception_essage = "元素定位失败"
        # if "Could not start a new session. Possible causes are invalid address of the remote server or browser start-up failure  "in str(e):
        #     Common.exception_essage = "Appium创建session失败"
        # if "A new session could not be created." in str(e):
        #     Common.exception_essage = "Appium创建session失败"
        # print u"异常原因： ",Common.exception_essage
        #
        # 截屏
        file_path = com.take_screenShot(driver)
        try:
            com.send_mail_warning(e, file_path)
        except Exception as e:
            print e.message
