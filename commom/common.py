# -*- coding: UTF-8 -*-
#author：zhongqin

import ConfigParser
import os
import smtplib
import sys
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

from selenium.webdriver.common.by import By

import read_config
from commom.my_logging import Logging
from page_elements.element_public import ElementPublic

reload(sys)
sys.setdefaultencoding('utf8') 
"""
此类用于实现公用的方法，例如初始化，文本查找，元素查找等
__init__ ：初始化，读取配置文件
start_appium ：启动appium
setUp_appium ：设置初始化appium
error_catch_appium：Appium Server错误处理
reStart_AdbProcess：重启adb
killPid_By_Port(self, portNum)：根据端口号获取进程id，并杀死进程

"""
count = 0
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

cf = read_config.ReadConfig()

class Common:
    global pass_condition
    global test_case_Id
    global test_case_name
    global element_public
    element_public = ElementPublic()
    log = Logging()

    def __init__(self):
        #读取配置档
        try:
            # cf = ConfigParser.ConfigParser()
            # cf.read(os.path.join(mysend.abs_path, "config.conf"))

            self.loginUsername=cf.get('login','loginUsername')
            self.loginPwd = cf.get('login', 'loginPwd')
            self.sendUsername = cf.get('send', 'sendUsername')
            self.sendTo = cf.get('send', 'sendTo')
            self.sendPwd = cf.get('send', 'sendPwd')
            self.hostPort=cf.get('send','hostPort')
            self.tester = cf.get('send', 'tester')
            self.orderUsername = cf.get('order', 'orderUsername')
        except Exception as e:
            print "read configfile fail"
            print e.message

    #等待文本出现 15秒超时
    def is_text_exist(self,driver,text):
        count = 0
        while(not self.wait_text(driver,text)):
            if(count > 10):
                print "文本：",text,"查找超时"
                return False
            else:
                sleep(1)
                count +=1
        return True

    #判断文本是否出现
    def wait_text(self,driver,text):
        flag = False
        try:
            xpt = "//*[contains(@text,'"+text+"')]"
            element = driver.find_element(by=By.XPATH,value=xpt)
            # element = Common.driver.find_element(by=By.NAME,value=text)

            flag = None!=element
        except Exception as e:
            print e.message
        return flag

    def is_element_exist(self,driver,by_type,locator):
        count = 0

        while(not self.wait_element(driver,by_type,locator)):
            if(count>15):
                self.log.logStep(u"元素：" + locator + "查找超时")
                return False
            else:
                sleep(1)
                count+=1
        return True

    #等待元素出现
    def wait_element(self,driver,by_type, locator):
        flag = False
        try:
            element = driver.find_element(by=by_type,value=locator)
            flag = None!=element
        except Exception as e:
            print e.message
        return flag

    def send_mail_warning(self,e_msg, file_path):
        '''
        发送异常邮件提醒
        e_msg:异常原因
        file_path:截图路径
        mail_to:收件人
        '''
        msg = MIMEMultipart('related')
        msg['From'] = self.sendUsername
        # mail_to = ('qin.zhong@mangocity.com','tiezhu.liu@mangocity.com','hong.hao@mangocity.com')
        mail_to = self.sendTo.split(',')
        to_list = []
        for lis in mail_to:
            to_list.append(lis)
        msg['To'] = self.sendTo
        info_excp_prompt = element_public.INFO_EXCP_PROMPT.split(',')
        msg['Subject'] = info_excp_prompt[0] + Common.test_case_Id + info_excp_prompt[1] + Common.test_case_name + info_excp_prompt[2] + time.strftime('%Y-%m-%d %X', time.localtime())
        print msg['Subject']
        send_content = element_public.SEND_CONTENT.split(',')
        content = send_content[0] + time.strftime('%Y-%m-%d %X', time.localtime()) + send_content[1] + send_content[2] + str(e_msg) +send_content[3]# 邮件内容
        print "content:", content
        msgtxt = MIMEText(content, 'html', 'utf-8')

        msg.attach(msgtxt)
        if file_path == "" or file_path == None:
            print u"异常邮件没有截图"
        else:
            # 添加截图附件
            fp = open(file_path, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            msgImage.add_header('Content-ID', '<image1>')
            msg.attach(msgImage)
            msg.attach(MIMEText("""<br><img src="cid:image1"></br>""", 'html', 'utf-8'))

        # 发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.hostPort)
            print smtp.login(self.sendUsername, self.sendPwd)

            smtp.sendmail(msg['From'], to_list, msg.as_string())
            smtp.quit()
            print '::info::异常邮件提醒发送完成'

        except Exception as e:
            print u"发送异常邮件提醒失败"
            print e.message
        # # 重新初始化appium
        # print u"重新初始化appium"
        # try:
        #     self.killPid_By_Port(self.portNum)
        # except IOError as e:
        #     print e.message
        # self.error_catch_appium()  # appium server异常处理 并重启appium
        # self.setUp_appium()

    def take_screenShot(self,driver):
        '''截屏'''
        date = time.strftime('%Y-%m-%d', time.localtime())  # 获取作为截图文件夹名称
        # path = "../results/screenshot/" + date
        path = os.path.join(read_config.abs_path, "results\screenshot\\") + date
        if not os.path.exists(path):
            os.mkdir(path)
        pic_nmae = Common.test_case_Id + "_" + Common.test_case_name + "_" + time.strftime('%Y%m%d%H%M%S', time.localtime()) + ".png"
        full_path = path + "\\" + pic_nmae
        try:
            driver.get_screenshot_as_file(full_path)  # 截图 ，获取当前的屏幕截图,使用完整的路径 selenium webdriver内置方法

        except IOError as e:
            print e.message
        print u"已完成本次截屏：", full_path
        return full_path


if __name__ == "__main__":
    pass
    com = Common()
    com.send_mail_warning("测试","E:/mangoAppiumTest/results/screenshot/2016-04-20/002003_20160420155623.png")
    # # com.take_cmd("taskkill /f /im node.exe")
    # # thread.start_new_thread(com.my_start,(com.portNum,))
    # # t = Thread(target=com.my_start, args=(com.portNum,))
    # # t.start()
    # com.start_appium()
    # # sleep(3)
    # com.setUp_appium()
    # sleep(3)
    # driver = com.driver
    # driver.find_element_by_id("mangocity.activity:id/with_the_group").click()
    # print Common.is_text_exist("跟团游")
    # content = "<html><body><p>&nbsp;&nbsp;拨测时间：</p>" + Utility.get_current_time() + "<br/>" + "&nbsp;&nbsp;异常情况：" + "111" + "<br/></body></html>"
    # print content




