#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from configparser import RawConfigParser
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# ========================================================================获取proxy设置
def get_proxy_info():
    # 初始化变量
    proxies = {}
    proxy_info = {}
    cookie = {}
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')

    # 获取设置值
    proxy_type = config.get('proxy', 'type')
    proxy = config.get('proxy', 'proxy')
    timeout = config.getint('proxy', 'timeout') # 单位秒
    retry_count = config.getint('proxy', 'retry')
    if proxy_type == 'http':
        proxies = {"http": "http://" + proxy, "https": "http://" + proxy}
    elif proxy_type == 'socks5':
        proxies = {"http": "socks5h://" + proxy, "https": "socks5h://" + proxy}
    try:
        cookies_value = config.get('Cookies', 'javdb')
        if cookies_value:
            cookie = {'cookie':cookies_value}
        else:
            cookie = None
    except:
        cookie =  None

    # 输出info
    proxy_info['proxy_type'] = proxy_type
    proxy_info['proxy'] = proxy
    proxy_info['timeout'] = timeout
    proxy_info['retry_count'] = retry_count
    proxy_info['proxies'] = proxies
    proxy_info['cookie'] = cookie

    return proxy_info


# ========================================================================网页请求
def get_html(url, cookies=None, headers=None):
    # 获取代理信息
    proxy_info = get_proxy_info()
    proxies = proxy_info.get('proxies')
    timeout = proxy_info.get('timeout')
    retry_count = proxy_info.get('retry_count')

    if not headers:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    i = 0
    ex1 = 'Error in get_htm3l url: ' + url
    while i < retry_count:
        try:
            getweb = requests.get(str(url), headers=headers, cookies=cookies, proxies=proxies, timeout=timeout, verify=False)
            getweb.encoding = 'utf-8'
            return True, getweb.text
        except Exception as ex:
            i += 1
            ex1 = str(ex)
            print('[-]Connect retry ' + str(i) + '/' + str(retry_count) + ' ' + ex1)
    return False, ex1


def post_html(url: str, query: dict, headers={}):
    # 获取代理信息
    proxy_info = get_proxy_info()
    proxies = proxy_info.get('proxies')
    timeout = proxy_info.get('timeout')
    retry_count = proxy_info.get('retry_count')

    for i in range(retry_count):
        try:
            result = requests.post(url=url, data=query, headers=headers, proxies=proxies, timeout=timeout)
            result.encoding = 'utf-8'
            result = result.text
            return True, result
        except Exception as error_info:
            error_info1 = 'Error in post_html2 :' + str(error_info)
            print("[-]Connect retry {}/{}".format(i + 1, retry_count) + ' ' + str(error_info))
    print("[-]Connect Failed! Please check your Proxy or Network!")
    print('Error in post_html2:' + error_info1)
    return False, error_info1
