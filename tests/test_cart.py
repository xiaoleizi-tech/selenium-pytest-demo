#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/5/28 12:54
from page.inventory_page import InventoryPage


def test_inventory(login):
    inventory = InventoryPage(login)
    # Sauce Labs Backpack到购物车
    inventory.add_to_cart("Sauce Labs Backpack")
    # 断言购物车数量为 1
    assert inventory.get_cart_count() == 1
    # 加入 Sauce Labs Bike Light 到购物车,断言购物车数量为 2
    inventory.add_to_cart("Sauce Labs Bike Light")
    assert inventory.get_cart_count() == 2
    # 点击购物车图标进入购物车页面
    inventory.go_to_cart()
    # 断言URL包含 cart.html
    assert "cart.html" in login.current_url, f"预期进入购物车页，实际URL：{login.current_url}"