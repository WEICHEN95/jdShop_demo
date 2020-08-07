import time
import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
# 添加保持登录的数据路径：
option.add_argument(r"user-data-dir=C:\Users\2019\AppData\Local\Google\Chrome\User Data")
# option.add_argument('headless')
chrome_driver = r"C:\Users\2019\AppData\Local\Programs\Python\Python36\chromedriver.exe"
# 初始化driver
driver = webdriver.Chrome(chrome_driver, chrome_options=option)
driver.get('https://product.shop.jd.com/rest/ware/list/manage?wareStatusStr=onSale&firstQuery=1')
driver.maximize_window()
print('RP瑞普专卖店自动化启动：' + '\n'
                        '1.请在15秒内扫码登录' + '\n'
                                        '2.请使用谷歌浏览器' + '\n'
                                                       '3.本程序会跳过相纸商品的修改' + '\n'
                                                                           '4.第一次使用此程序请先进行登录' + '\n'
                                                                                                '5.每发布一个商品会停留5秒，以免平台认为速度过快' + '\n')
driver.execute_script("alert('请在15秒内扫码，进入自动化操作。')")
time.sleep(15)
# 获取修改商品<div>
try:
    elements = driver.find_elements_by_class_name('current-item')
except Exception as err:
    print('未找到商品，请确认是否用手机扫描二维码登录,并关闭浏览器重新启动程序！')

# 点击修改商品<a>
for num in range(10):
    driver.get('https://product.shop.jd.com/rest/ware/list/manage?wareStatusStr=onSale&firstQuery=1')
    time.sleep(3)
    try:
        driver.execute_script('document.documentElement.scrollTop=' + str(400 + num * 120))
        psku = driver.find_elements_by_class_name('p-sku')[num].text
        title = driver.find_elements_by_class_name('editTitleLink')[num].text
        if title.find('相纸') > -1:
            print('第' + str(num + 1) + '个商品为相纸，不做修改.')
            continue
        elements = driver.find_elements_by_class_name('current-item')
        elements[num].click()
    except Exception as err:
        print('第' + str(num + 1) + 'B:')
        # print(psku)
        print(err)
        continue
    time.sleep(1)

    try:
        driver.find_element_by_link_text('修改商品').click()
    except Exception as err:
        pass

    try:
        # 将鼠标移到商品图片并删除商品展示图
        ActionChains(driver).move_to_element(driver.find_elements_by_class_name('rule-bot')[0]).perform()
        # 点击图片，以显示删除按钮
        driver.find_elements_by_class_name('l-img')[1].click()
        # 点击删除
        for i in range(8):
            driver.find_elements_by_class_name('f-r')[1].click()

        # 点击细节图
        driver.find_elements_by_class_name('img-up')[2].click()
        # 选择一张属性为‘img-con img-revert’的图片，点击
        time.sleep(3)
        elements = driver.find_elements_by_class_name('img-con')
        k = 0
        alist = random.sample(range(1, 20), 19)  # random.sample()生成不相同的随机数
        for i in alist:
            if elements[22 + i].get_attribute('class') == 'img-con img-revert':
                continue
            elements[22 + i].click()
            k += 1
            if k == 9:
                break
        time.sleep(3)
        # 滚轮
        driver.execute_script('document.documentElement.scrollTop=1600')
        # 点击关闭、
        driver.find_elements_by_class_name('pop-icon-close')[2].click()
        # 点击保存
        es = driver.find_elements_by_class_name('pop-btn-primary')
        for e in es:
            if e.text == '保存':
                e.click()
                break
        time.sleep(4)
        for m in range(len(driver.find_elements_by_class_name('pop-btn-ghost'))):
            es = driver.find_elements_by_class_name('pop-btn-ghost')[m]
            if es.text == '直接发布' or es.text == '发布商品':
                es.click()
                break
        time.sleep(4)
        # 返回商品列表页
        try:
            driver.find_element_by_link_text('查看商品').text == '查看商品'
        except Exception as err:
            print('第' + str(num + 1) + '商品未发布')
            print(psku)
            print(err)
            print('------------------------------------------------')
            continue
    except Exception as err:
        print('>第' + str(num + 1) + 'A:')
        print(psku)
        print(err)
        continue
    print('第' + str(num + 1) + '个商品修改发布完成.')
    print(psku)
