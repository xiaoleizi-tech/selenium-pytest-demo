#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/5/27 21:54
import pytest
import undetected_chromedriver as uc
from page.login_page import LoginPage


@pytest.fixture(scope="session")
def driver():
    wd = uc.Chrome(driver_executable_path=r"C:\chromedriver\chromedriver.exe")
    wd.implicitly_wait(10)
    # 共同使用一个driver
    yield wd
    # 用例执行完，退出浏览器
    wd.quit()


@pytest.fixture()
def login(driver):
    # 测试前登录
    login_page = LoginPage(driver)
    login_page.driver.get("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")
    yield driver
