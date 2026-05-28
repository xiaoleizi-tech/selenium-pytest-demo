# Selenium + Pytest 自动化测试项目

基于 Python 的 Web 自动化测试项目，采用 PO 模式设计。

## 技术栈
- Python 3.12
- Selenium 4
- Pytest 9
- undetected-chromedriver

## 项目结构
firstProject/
├── conftest.py          # 全局fixture（浏览器、登录）
├── page/                # 页面对象层（PO模式）
│   ├── login_page.py
│   └── inventory_page.py
└── tests/               # 测试用例层
├── test_login.py
└── test_cart.py
## 测试用例
- 登录成功 / 失败测试
- 参数化测试（多用户登录）
- 购物车操作测试

## 运行
```bash
pytest tests/ -v
```
