#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/5/27 21:55
import pytest
from selenium.webdriver.common.by import By

from page.login_page import LoginPage

url = "https://www.saucedemo.com"


def test_login(driver):
    # 用 driver fixture 启动浏览器
    login_page = LoginPage(driver)
    # 打开 https://www.saucedemo.com
    login_page.driver.get(url)
    # 用 LoginPage 类完成登录操作
    login_page.login("standard_user", "secret_sauce")
    assert login_page.driver.title == "Swag Labs"


def test_login_fail(driver):
    # 用 driver fixture 启动浏览器
    login_page = LoginPage(driver)
    # 打开 https://www.saucedemo.com
    login_page.driver.get(url)
    # 用错误的密码
    login_page.login("standard_user", "secret_sauc")
    # assert "Username and password do not match" in login_page.driver.page_source
    error_msg = login_page.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in error_msg


@pytest.mark.parametrize(
    "username, password,expected_result,should_succeed",
    [("standard_user", "secret_sauce", "登录成功", True),
     ("locked_out_user", "secret_sauce", "显示用户被锁定", False),
     ("problem_user", "secret_sauce", "登录成功", True)]
)
def test_login_three(driver, username, password, expected_result, should_succeed):
    # 用 driver fixture 启动浏览器
    login_page = LoginPage(driver)
    # 打开 https://www.saucedemo.com
    login_page.driver.get(url)
    # 用 LoginPage 类完成登录操作
    login_page.login(username, password)
    if should_succeed:
        # 登录成功的断言
        assert login_page.driver.title == "Swag Labs", f"预期: {expected_result}, 实际登录失败"
    else:
        # 登录失败的断言（出现错误提示）
        error_msg = login_page.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "locked out" in error_msg, f"预期: {expected_result}, 实际没出现锁定提示"
