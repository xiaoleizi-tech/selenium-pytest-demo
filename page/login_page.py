#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/5/27 21:55
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
