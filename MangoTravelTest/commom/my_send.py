# -*- coding: utf-8 -*-
import ConfigParser
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import time

import read_config

cf = read_config.ReadConfig()

class SendMail:

    def __init__(self):
        # 读取配置档
        try:
            # cf = ConfigParser.ConfigParser()
            # cf.read(cf.read(os.path.join(abs_path, "config.conf")))

            self.sendUsername = cf.get('send', 'sendUsername')
            self.sendTo = cf.get('send', 'sendTo')
            self.sendPwd = cf.get('send', 'sendPwd')
            self.hostPort = cf.get('send', 'hostPort')
            self.tester = cf.get('send', 'tester')
        except Exception as e:
            print "read configfile fail"
            print e.message


    def parse_lis(self,lis):
        '''解析每个模块返回的通过率   每个模块一个python文件 包含该模块所有测试用例'''
        pass_count = 0
        for each_lis in lis:
            if each_lis[3] == True:
                pass_count += 1
        total_count = len(lis)
        fail_count = total_count - pass_count
        pass_percent = "%.2f%%" % (pass_count * 100.0 / total_count)  # 通过率
        ret_lis=[lis[0][0],total_count,pass_count,fail_count,pass_percent]
        return ret_lis #返回模块名称，总用例数，成功个数，失败个数，通过率

    def sen_mail(self, lis):
        """
        测试完成之后发送结果邮件
        lis:每个模块的测试结果集[list1,list2......]
        """
        login_user = self.sendUsername
        login_pwd = self.sendPwd
        host_port = self.hostPort
        mail_to = self.sendTo.split(',')
        to_list = []
        for each_mail in mail_to:
            to_list.append(each_mail)

        msg = MIMEMultipart('related')
        msg['From'] = self.sendUsername

        msg['To'] = self.sendTo
        msg['Subject'] = u"测试—芒果旅游app自动化拨测报告" + u"(时间：" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
        tr_tr_mokuai_info = ''
        len_lis = len(lis)
        if len_lis != 0:
            print "lis:", lis
            if lis[0][3] != 0:  # 有失败用例 标红
                tr_td_mokuai_info = "<tr style = 'color:red;'><td style='border:1px solid #999999;height:20px;font-size:12px;width:130px' rowspan =" + str(len_lis) + ">芒果旅游</td>" \
                                    "<td style='border:1px solid #999999;height:20px;font-size:12px;width:130px'>" + str(lis[0][0]) + "</td>" \
                                    "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(lis[0][1]) + "</td>" \
                                    "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(lis[0][2]) + "</td>" \
                                    "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + str(lis[0][3]) + "</td>" \
                                    "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + str(lis[0][4]) + "</td>" \
                                    "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + self.tester + "</td></tr>"
            else:
                tr_td_mokuai_info = "<tr><td style='border:1px solid #999999;height:20px;font-size:12px;width:130px' rowspan =" + str(len_lis) + ">芒果旅游</td>" \
                                    "<td style='border:1px solid #999999;height:20px;font-size:12px;width:130px'>" + str(lis[0][0]) + "</td>" \
                                    "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(lis[0][1]) + "</td>" \
                                    "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(lis[0][2]) + "</td>" \
                                    "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + str(lis[0][3]) + "</td>" \
                                    "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + str(lis[0][4]) + "</td>" \
                                    "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + self.tester + "</td></tr>"
            for each_lis in lis[1:]:
                print "each_lis,", each_lis
                if int(each_lis[3]) != 0:
                    tr_td_mokuai_info += "<tr style = 'color:red;'><td style='border:1px solid #999999;height:20px;font-size:12px;width:130px'>" + str(each_lis[0]) + "</td>" \
                                         "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(each_lis[1]) + "</td>" \
                                         "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(each_lis[2]) + "</td>" \
                                         "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + str(each_lis[3]) + "</td>" \
                                         "<td style='font-size:12px;border:1px solid #999999;height:20px;color:red;'>" + str(each_lis[4]) + "</td>" \
                                         "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + self.tester + "</td></tr>"
                else:
                    tr_td_mokuai_info += "<tr><td style='border:1px solid #999999;height:20px;font-size:12px;width:130px'>" + str(each_lis[0]) + "</td>" \
                                       "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(each_lis[1]) + "</td>" \
                                       "<td style='border:1px solid #999999;height:20px;font-size:12px;'>" + str(each_lis[2]) + "</td>" \
                                       "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + str(each_lis[3]) + "</td>" \
                                       "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + str(each_lis[4]) + "</td>" \
                                       "<td style='font-size:12px;border:1px solid #999999;height:20px;'>" + self.tester + "</td></tr>"
        if tr_td_mokuai_info:
            html_info_mokuai_tablelist = "<table style='width:100%;border-collapse:collapse;font-size:12px;'><th style='background-color:#ccc;border:1px solid #999999;height:15px;font-size:12px;'>产品</th>" \
                                         "<th style='background-color:#ccc;border:1px solid #999999;height:15px;font-size:12px;'>模块名称</th>" \
                                         "<th style='background-color:#ccc;border:1px solid #999999;height:15px;font-size:12px;'>用例总数</th>" \
                                         "<th style='background-color:#ccc;border:1px solid #999999;height:15px;font-size:12px;'>成功用例数</th>" \
                                         "<th style='font-size:12px;border:1px solid #999999;height:15px;background-color:#ccc;'>失败用例数</th>" \
                                         "<th style='font-size:12px;border:1px solid #999999;height:15px;background-color:#ccc;'>成功率</th>" \
                                         "<th style='font-size:12px;border:1px solid #999999;height:15px;background-color:#ccc;'>测试人员</th></tr>" + tr_td_mokuai_info + "</table>"

        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        txt = MIMEText(
                '<html><body><p>Hello,All:</p><br/><p>&nbsp;&nbsp;&nbsp以下是本次芒果旅游自动化功能拨测情况,请查阅：<br/>' +
                '<br/>&nbsp;&nbsp;结束时间：<br/>' + "&nbsp;&nbsp;" + end_time+
                 '<br/>&nbsp;&nbsp;各模块拨测展示：<br/>' + "&nbsp;&nbsp;&nbsp;" + html_info_mokuai_tablelist +
                "<br/></body></html>", 'html', 'utf-8')

        msg.attach(txt)
        # 发送邮件
        try:

            smtp = smtplib.SMTP()
            smtp.connect(host_port)
            print smtp.login(login_user, login_pwd)
            print "发送测试报告邮件inggggggg "
            smtp.sendmail(msg['From'], to_list, msg.as_string())
            smtp.quit()
            print '::info::[mysend.py send_mail 邮件发送完成]'
            return 1, "Done"
        except Exception, e:
            return 0, e
if __name__=="__main__":
    cf = ConfigParser.ConfigParser()
    cf.read("config.conf")
    sendUsername = cf.get('send', 'sendUsername')
    print sendUsername


    # cf = ConfigParser.ConfigParser()
    # cf.read("config.conf")
    # loginUsername = cf.get('login', 'loginUsername')
    # print loginUsername














