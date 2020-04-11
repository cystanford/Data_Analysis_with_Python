# 自动登录开课吧学习中心 提交表单
import time
from selenium import webdriver

# 需要将chromedriver放到Chrome\Application目录下
driver = webdriver.Chrome()

request_url = 'http://student.kaikeba.com/user/login'
driver.get(request_url)

driver.find_element_by_id('username').send_keys('13520355196')
driver.find_element_by_id('password').send_keys('helloworld')
driver.find_element_by_class_name('submit').click()
