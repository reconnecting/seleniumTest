import unittest
from  web_ui.testKeywordDemo import TestKeywords
import time
from ddt import ddt,data,unpack

url = "http://www.baidu.com"

@ddt
class TestForKey(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.tk = TestKeywords("chrome", url)

    def tearDown(self):
        print('teardown')
        time.sleep(3)
        self.tk.quit_browser()

    @data(['id','自动化测试'],['id','单元测试'])
    @unpack  #需要增加一个unpack的方法把数据解包
    def test_1(self, locator,input_value):
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element('xpath', '//*[@id="su"]')

    def test_2(self):
        print('test2,print')

if __name__ == '__main__':
    unittest.TestCase