from basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage(BasePage):

    # 把页面所用到的元素全部都提取出来
    input_id = (By.ID,'kw')
    click_id = (By.ID, 'su')


    # 输入文字
    def input_text(self, text):
        self.locator(self.input_id).send_keys(text)

    # 点击元素
    def click_element(self):
        self.locator(self.click_id).click()

    def check(self,input_text):
        self.visit()
        self.input_text(input_text)
        self.click_element()

    # 双击元素
    def dubble_click(self):
        self.locator(self.click_id).double_click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    sp.check("阿凡达")
