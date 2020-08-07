import time
import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
# 添加保持登录的数据路径：
# option.add_argument(r"user-data-dir=C:\Users\2019\AppData\Local\Google\Chrome\User Data")
# option.add_argument('headless')
chrome_driver = r"C:\Users\2019\AppData\Local\Programs\Python\Python36\chromedriver.exe"
# 初始化driver
driver = webdriver.Chrome(chrome_driver, chrome_options=option)
driver.get('chrome://version')
driver.maximize_window()