import time
import random
import sys
# from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# option = webdriver.ChromeOptions()
# 添加保持登录的数据路径：
# option.add_argument(r"user-data-dir=C:\Users\2019\AppData\Local\Google\Chrome\User Data")
# option.add_argument('headless')
chrome_driver = r"C:\Users\2019\AppData\Local\Programs\Python\Python36\chromedriver.exe"
# 初始化driver
# driver = webdriver.Chrome(chrome_driver, chrome_options=option)
# driver.get('chrome://version')
# driver.maximize_window()
print(sys.executable[:-10])
# for i in sys.path:
#     print(i)
import os

cmd = 'pip install selenium'
# res = os.system(cmd)

import shutil

# 移动文件夹示例
shutil.move(r"C:/Users/2019/AppData/Local/Programs/Python/Python36/chromedriver.exe", sys.executable[:-10])
