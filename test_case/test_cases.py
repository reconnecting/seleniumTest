import unittest
from pageObject.search_page import SearchPage
from selenium import webdriver
from unit_demo.test_for_key import time_sleep_decorator
from ddt import ddt,data,unpack

driver = webdriver.Chrome()

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.sp = SearchPage(driver)

    @time_sleep_decorator
    def tearDown(self):
        self.sp.quit_browser()

    @data('江峰','马化腾')
    def test_1(self, input):
        self.sp.check(input)

if __name__ == '__main__':
    unittest.main()