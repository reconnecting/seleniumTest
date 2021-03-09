from selenium import webdriver
from time import sleep

# 生成一个chromedriver
driver = webdriver.Chrome()


url = "http://www.baidu.com"
driver.get(url)

driver.find_element_by_id('kw').send_keys("自动化测试")

driver.find_element_by_id('su').click()

sleep(3)

driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
