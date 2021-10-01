#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import Function.config as cf
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# ========================================================================get请求
def get_html(url: str, cookies=None, headers=None):
    # 获取代理信息
    config = cf.get_config()
    proxies = config['proxies']
    timeout = config['timeout']
    retry = config['retry']

    if not headers:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    for i in range(retry):
        try:
            getweb = requests.get(str(url), headers=headers, cookies=cookies,
                                  proxies=proxies, timeout=timeout, verify=False)
            getweb.encoding = 'utf-8'
            return True, getweb.text
        except Exception as ex:
            e = ('GET: %s error: %s' % (url, ex))
            errin_info = ('[-]GET [%s/%s]: %s \n   error: %s' %
                          (i+1, retry, url, ex))
            print(errin_info)
    print("[-]Connect Failed! Please check your Proxy or Network!")
    return False, e


# ========================================================================post请求
def post_html(url: str, query: dict, headers={}):
    # 获取代理信息
    config = cf.get_config()
    proxies = config.get('proxies')
    timeout = config.get('timeout')
    retry = config.get('retry')

    for i in range(retry):
        try:
            result = requests.post(
                url=url, data=query, headers=headers, proxies=proxies, timeout=timeout)
            result.encoding = 'utf-8'
            result = result.text
            return True, result
        except Exception as ex:
            e = ('POST: %s error: %s' % (url, ex))
            errin_info = ('[-]POST [%s/%s]: %s \n   error: %s' %
                          (i+1, retry, url, ex))
            print(errin_info)
    print("[-]Connect Failed! Please check your Proxy or Network!")
    return False, e
