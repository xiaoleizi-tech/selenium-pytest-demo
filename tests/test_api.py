#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/5/28 20:40

import requests


def test_api():
    response = requests.get('https://httpbin.ceshiren.com/get')
    print("状态码：", response.status_code)
    print("响应内容：", response.text)
    assert response.status_code == 200


def test_post():
    response = requests.post(url='https://httpbin.ceshiren.com/post', json={
        "username": "zhulei",
        "password": "123456"
    })
    print(response.json()["json"])
    assert response.status_code == 200


def test_get():
    params = {"name": 'zhulei', "city": "chengdu"}
    response = requests.get(url='https://httpbin.ceshiren.com/get', params=params)
    print(response.json()["args"])
    assert response.json()["args"]["name"] == "zhulei"


def test_headers():
    headers = {
        "Authorization": "Bearer abc123token",
        "User-Agent": "MyTestApp/1.0"
    }
    response = requests.get(url='https://httpbin.ceshiren.com/get', headers=headers)
    print(response.json()["headers"])
    assert "Authorization" in response.json()["headers"]


def test_post1():
    js = {
        "username": "zhulei",
        "password": "123456"
    }
    res = requests.post(url='https://httpbin.ceshiren.com/post', json=js)
    print(res)


def test_token_flow():
    url1 = "https://httpbin.ceshiren.com/post"
    json = {"username": "zhulei", "password": "123456"}
    res = requests.post(url=url1, json=json)
    token = res.json()["origin"]
    print("拿到的token：", token)
    headers = {"Authorization": f"Bearer {token}"}
    url2 = "https://httpbin.ceshiren.com/get"
    profile_res = requests.get(url=url2, headers=headers)
    rec = profile_res.json()["headers"]["Authorization"]
    print("第2个接口收到的token:", rec)
    assert token in rec
