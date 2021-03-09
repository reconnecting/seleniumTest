from selenium import webdriver
import logging

# logging.basicConfig('debug')
url = "http://www.baidu.com"

class TestKeywords(object):

    def __init__(self,browser_type, url):
        self.driver = self.open_browser(browser_type)
        self.driver.get(url)

    def open_browser(self, browser_type):
        # 判断浏览器类型并打开
        if browser_type == "chrome":
            self.driver = webdriver.Chrome()
            return self.driver
        elif browser_type == "firefox":
            self.driver = webdriver.Firefox()
        else:
            print("type error")

    def locator(self, locator_type, value):
        # 通过元素类型值定位元素
        if locator_type == "id":
            element = self.driver.find_element_by_id(value)
            return element
        elif locator_type == "xpath":
            element = self.driver.find_element_by_xpath(value)
            return element
        elif locator_type == "name":
            element = self.driver.find_element_by_name(value)
            return element

    def input_text(self, locator_type, value, text):
        # 输入一个text
        self.locator(locator_type, value).send_keys(text)

    def click_element(self,locator_type, value):
        # 点击操作
        self.locator(locator_type, value).click()


if __name__ == '__main__':
    tk = TestKeywords("chrome", url)
    tk.input_text('id', 'kw', "自动化测试")
    tk.click_element('xpath','//*[@id="su"]')