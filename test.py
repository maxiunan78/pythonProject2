#!/usr/bin/env python
#-*- coding:utf-8 -*-
import selenium
from selenium.webdriver import Remote
from selenium.webdriver import Chrome
from  selenium import webdriver

from time import sleep
import unittest

def tryf():
    # driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                 desired_capabilities={'platform':'ANY',
    #                                     'browserName':'chrome',
    #                                     'version':'',
    #                                     'javascriptEnabled':'True'}
    #             )
    #
    # driver.get('http://www.baidu.com')
    # driver.find_element_by_id("kw").send_keys("remote")
    # driver.find_element_by_id("su").click()

    #

    global driver
    driver = Chrome()
    # driver = Chrome(executable_path=r'C:\Users\ASUS\AppData\Local\Google\Chrome\Application')
    driver.get("https://wx.youzhanguanjia.com/web/indexV10.0.html?version=V10.0#/centerIndex?openId=o1dr10QhX4pTj4QsyNYMLhmQXHIM&hqId=16548&stationId=165481000&hasWXPay=1&isMember=1&memberId=131091122")
    # driver.find_element_by_xpath("//input[@name='mobile']").send_keys("wl003")
    # driver.find_element_by_xpath("//input[@name='password']").send_keys("qwer1234")
    # driver.find_element_by_xpath(("//button[@type='button']")).click()


    listcookies = [

        {
            'domain': 'wx.youzhanguanjia.com',
            'name': 'JSESSIONID',
            'value': 'ECAC5519FE3810AD663ECE3B960BDD22'

        },
        {
            'domain': 'wx.youzhanguanjia.com',
            'name': 'WX_COOKIE_OP',
            'value': 'o1dr10eRSZ0xtNfcZ_JzcTefMElI'
        },
        {
            'domain': 'wx.youzhanguanjia.com',
            'name': 'WX_COOKIE_ME',
            'value': '131091122'
        },
        {
            'domain': 'wx.youzhanguanjia.com',
            'name': 'WX_COOKIE_HQ',
            'value': '16548'
        },
        {
            'domain': 'wx.youzhanguanjia.com',
            'name': 'token',
            'value': 'WX_ede138987c004acba4c7a1309fda83ee'
        },
        {
            'domain': 'wx.youzhanguanjia.com',
            'name': 'acw_tc',
            'value': '3da0e4a816372259813763986e8e2cacf60e30d94f00959ffee63159ef'
        }
        ]


    for cookies in listcookies:

        driver.add_cookie(cookie_dict=cookies)
    # driver.implicitly_wait(10)
    #
    # driver = webdriver.Firefox()
    # driver.get("htttp://www.youdao.com")
    driver.get(
        "https://wx.youzhanguanjia.com/web/indexV10.0.html?version=V10.0#/centerIndex?openId=o1dr10QhX4pTj4QsyNYMLhmQXHIM&hqId=16548&stationId=165481000&hasWXPay=1&isMember=1&memberId=131091122")
    # driver.quit()

if __name__== '__main__':
    tryf()
