#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/5/27 23:55
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        """把指定商品加入购物车"""
        # 找到商品转换成加入购物车元素按钮id
        add_but_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        # 通过id扎到添加购物车按钮元素,点击加入购物车
        self.driver.find_element(By.XPATH, f'//*[@id="{add_but_id}"]').click()

    def get_cart_count(self):
        """获取购物车数量（返回数字）"""
        # 获取购物车数量，没商品时返回0
        try:
            badge = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        """点击购物车图标进入购物车页面"""
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
