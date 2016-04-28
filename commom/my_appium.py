# -*- coding: utf-8 -*-
import ConfigParser
import os
import subprocess
from threading import Thread
from time import sleep

from appium import webdriver

import read_config

cf = read_config.ReadConfig()

global driver
driver = None
count = 0
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class MyAppium:
    def __init__(self):
        # 读取配置档
        try:
            # cf = ConfigParser.ConfigParser()
            # cf.read(os.path.join(mysend.abs_path, "config.conf"))
            self.phoneID = cf.get('phone', 'phoneID')
            self.portNum = cf.get('phone', 'portNum')
            self.platformName = cf.get('phone', 'platformName')
            self.platformVersion = cf.get('phone', 'platformVersion')
            self.deviceName = cf.get('phone', 'deviceName')
            self.appPackage = cf.get('activty', 'appPackage')
            self.appActivity = cf.get('activty', 'appActivity')
            self.baseUrl = 'http://127.0.0.1:' + self.portNum + '/wd/hub'
        except Exception as e:
            print "read configfile fail"
            print e.message

    # 启动appium
    def start_appium(self):
        cmd = 'cmd.exe /k appium -a 127.0.0.1 -p ' + self.portNum
        subprocess.call("taskkill /f /im CMD.exe /im cmd.exe")
        t = Thread(target=self.take_cmd, args=(cmd,))
        t.start()
        sleep(5)
        print "start appium success"
        # t.join(10)

    #关闭appium
    def quit_appium(self):
        cmd = "taskkill /f /im node.exe"
        t = Thread(target=self.take_cmd, args=(cmd,))
        t.start()

    def take_cmd(self, cmd):
        try:
            subprocess.call(cmd)
        except Exception as e:
            print e.message

    def restart_appium(self):
        self.quit_appium()
        self.start_appium()

    # 设置appium
    def setUp_appium(self):
        global count
        if count < 3:
            try:
                desired_caps = {}
                desired_caps['platformName'] = self.platformName
                desired_caps['platformVersion'] = self.platformVersion
                # desired_caps['app'] = PATH('E:/MyFTP/' + sys.argv[1] + '/app-release.apk')
                # desired_caps['app'] = PATH('../app/app-release.apk')
                desired_caps['deviceName'] = self.deviceName
                desired_caps['appPackage'] = self.appPackage
                desired_caps['appActivity'] = self.appActivity
                desired_caps['unicodeKeyboard']=True
                desired_caps['resetKeyboard']=True

                MyAppium.driver = webdriver.Remote('http://127.0.0.1:' + self.portNum + '/wd/hub', desired_caps)
                sleep(5)
                # driver.set_page_load_timeout(30)
                print "初始化Appium Driver成功"
                count = 0
            except:
                count += 1
                print "初始化Appium Driver失败，进入异常处理并重新启动Appium，重新初始化Appium Driver"
                print "尝试次数： " ,count
                self.restart_appium()#关闭appium server
                sleep(2)
                self.setUp_appium()
        else:
            print "初始化Appium Driver失败3次，重新初始化Adb"
            try:
                count = 0
                sleep(3)
                self.reStart_AdbProcess()  # 重启adb
                self.restart_appium()#关闭appium server 并重启appium
                self.setUp_appium()
            except Exception as e:
                print e.message
        return MyAppium.driver

      # 重启adb

    def reStart_AdbProcess(self):
        try:
            cmd = "cmd.exe /k start wmic process where name='adb.exe' call terminate"
            os.system(cmd)
            sleep(2)
            cmd = "cmd.exe /k start adb devices"
            os.system(cmd)
        except Exception as e:
            print e.message

    # 根据端口号获取进程，并杀死进程
    def killPid_By_Port(self, portNum):
        '''  现在没用，以后备用，别删了！'''
        cmd = "netstat -ano | findstr " + portNum
        ret = os.popen(cmd)
        line = ret.readline()
        print "line ", line
        if line == None or line == "":
            print "pid is null"
        else:
            proc = line.split()
            proc_id = proc[len(proc) - 1]
            print "proc_id:", proc_id
            try:
                # subprocess.call("cmd.exe /k taskkill /F /pid " + proc_id)
                cmd = "cmd.exe /k taskkill /F /pid " + proc_id
                t = Thread(target=self.take_cmd, args=(cmd,))
                t.start()
                sleep(3)
                print u"关闭appium"
            except Exception as e:
                print e.message

