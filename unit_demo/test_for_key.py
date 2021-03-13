import unittest
from  web_ui.testKeywordDemo import TestKeywords
import time
from ddt import ddt,data,unpack

url = "http://www.baidu.com"

def time_sleep_decorator(func):
    def wrapper(*args,**kwargs):
        time.sleep(3)
        print("等待3秒")
        return func(*args,**kwargs)
    return wrapper

@time_sleep_decorator
def menthod_test():
    print("这个就是被装饰的函数")


@ddt
class TestForKey(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.tk = TestKeywords("chrome", url)

    @time_sleep_decorator
    def tearDown(self):
        print('teardown')
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