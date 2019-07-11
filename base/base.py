from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Base(object):
    # 初始化
    def __init__(self,driver):
        self.driver = driver
    # 查找元素
    def base_find(self,location,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(
            lambda x:x.find_element(*location))


    # 输入方法
    def base_input(self,location,text):
        ele = self.base_find(location)
        ele.clear()
        ele.send_keys(text)


     # 点击方法
    def base_click(self,location):
        self.base_find(location).click()