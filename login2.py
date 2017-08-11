#coding=utf8
from selenium import webdriver
import time

base_url = "https://www.baidu.com"
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#清除所有cookie
driver.delete_all_cookies()
driver.get(base_url)

cookie_1 = {u'domain': u'.baidu.com',
            u'name': u'BDORZ',
            u'value': u'B490B5EBXXXXXXXXXXXXXDA1598',
            u'expiry': 1490346310,
            u'path': u'/',
            u'httpOnly': False,
            u'secure': False}

cookie_2 = {u'domain': u'.baidu.com',
            u'name': u'BDUSS',
            u'value': u'tvVzJHbm9ZOGp0NVN-RVdzMm9kOVRyUGhUcDhhbUUtRzlzRUhLQ2pPMFJCMFZaSVFBQUFBJCQAAAAAAAAAAAEAAAC6Eq4bc3VuenFlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABF6HVkReh1ZZW',
            u'expiry': 1749459934,
            u'path': u'/',
            u'httpOnly': True,
            u'secure': False}

#添加cookie
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)
time.sleep(2)
driver.refresh()
1111
