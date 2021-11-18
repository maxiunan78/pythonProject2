#!/usr/bin/env python
#-*- coding:utf-8 -*-

#author:maxiunan
# import
#
# def main():
#     try:
#         global driver
#         driver = driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         driver.implicitly_wait(10)

import os
import unittest
from time import sleep
from appium import webdriver
import traceback

from selenium.webdriver.common import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import selenium
from appium import webdriver
import uiautomation
from time import sleep
import  uiautomation as auto

class Windows(object):
    def __init__(self,app,host='localhost',port=4723):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Windows'
        self.desired_caps['app']=app
        self.desired_caps['deviceName'] = 'WindowsPC'
        self.host = host
        self.port = port
        self.appVersion = None

        try:
            self.driver = webdriver.Remote('http://{}:{}/wd/hub'.format(self.host,self.port),self.desired_caps)
        except Exception as e:
            raise  AssertionError(e)
        self.wait = WebDriverWait(self.driver,3)
        #隐式等待
        self.driver.implicitly_wait(3)
if __name__ == '__main__':
    app = "C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
    notepad = Windows(app)
    wechatWindow = auto.WindowControl(searchDepth=1,Name="微信",ClassName="WeChatMainWndForPC")

    # notepad.driver.find_elements_by_windows_uiautomation()
    notepad.driver.find_element(By.NAME, '通讯录').click()
    notepad.driver.find_element(By.NAME, '搜索').click()
    sleep(1)
    # notepad.driver.find_element(By.NAME, '搜索').send_keys('201加油站')
    notepad.driver.find_element(By.NAME, '搜索').send_keys('生产环境加油站')
    sleep(0.5)
    # notepad.driver.find_element(By.XPATH, "//*[@Name='201加油站' and @LocalizedControlType='按钮']").click()
    notepad.driver.find_element(By.XPATH, "//*[@Name='生产环境加油站' and @LocalizedControlType='按钮']").click()
    # e = notepad.driver.find_element(By.NAME, '菜单名称').click()
    e = notepad.driver.find_element(By.NAME, '会员中心').click()
    # print(notepad.driver.page_source)

    sleep(0.5)
    # os.system("automation.py  -t1 -f")
    list = wechatWindow.ListControl(Name='')
    # print(list)
    iterm = wechatWindow.MenuItemControl(Name='个人中心').Click()
    # print(notepad.driver.contexts)

    # # # notepad.driver.find_element(By.XPATH,"//*[@LocalizedControlType='菜单项目'][1]").click()
    # # notepad.driver.find_element(By.XPATH, "//*[@LocalizedControlType='列表'][1]").click()
    # e = notepad.driver.find_element(By.XPATH, "//*[@LocalizedControlType='列表']")
    # print(e)
    # e1 = notepad.driver.find_element(By.XPATH, "//*[@Name='积分商城' and @LocalizedControlType='菜单项目']")
    # print(e1)
    # print(e1.is_displayed())
    # print(e1.is_enabled())
    # print(e1.is_selected())
    # # e = notepad.driver.find_element(By.XPATH, "//*[@Name='积分商城' and @LocalizedControlType='菜单项目']")
    # # e.click()
    #
    # # notepad.driver.execute_script("arguments[0].click();", e)
    #
    # # if notepad.driver.find_element(By.XPATH, "//*[@Name='积分商城' and @LocalizedControlType='菜单项目']").click():
    # #     print('1111')

    notepad.driver.close()



