from selenium import webdriver

url = "https://www.baidu.com/"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def locator(self, locator):
        return self.driver.find_element(*locator)

    def quit_browser(self):
        self.driver.quit()

    def visit(self, url=url):
        self.driver.get(url)
