import requests
import os
from configparser import RawConfigParser


# ========================================================================获取proxy
def get_proxy():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    proxy_type = config.get('proxy', 'type')
    proxy = config.get('proxy', 'proxy')
    timeout = config.getint('proxy', 'timeout')
    retry_count = config.getint('proxy', 'retry')
    return proxy_type, proxy, timeout, retry_count


# ========================================================================获取proxies
def get_proxies(proxy_type, proxy):
    proxies = {}
    if proxy == '' or proxy_type == '' or proxy_type == 'no':
        proxies = {}
    elif proxy_type == 'http':
        proxies = {"http": "http://" + proxy, "https": "http://" + proxy}
    elif proxy_type == 'socks5':
        proxies = {"http": "socks5h://" + proxy, "https": "socks5h://" + proxy}
    return proxies


# ========================================================================获取cookies
def get_cookies():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    dic = {}
    javdb = config.get('Cookies', 'javdb')
    dmm = config.get('Cookies', 'dmm')
    dic_javdb = {'javdb':{'Cookie':javdb}}
    dic_dmm = {'dmm':{'Cookie':dmm}}
    dic.update(dic_javdb)
    dic.update(dic_dmm)
    return dic


# ========================================================================网页请求
def get_html(url, cookies=None):
    proxy_type = ''
    retry_count = 0
    proxy = ''
    timeout = 0
    try:
        proxy_type, proxy, timeout, retry_count = get_proxy()
    except Exception as error_info1:
        print('Error in get_html1 :' + str(error_info1))
        print('[-]Proxy config error! Please check the config.')
    proxies = get_proxies(proxy_type, proxy)
    i = 0
    while i < retry_count:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',}
            getweb = requests.get(str(url), headers=headers, timeout=timeout, proxies=proxies, cookies=cookies, verify=False)
            getweb.encoding = 'utf-8'
            return 'ok', getweb.text
        except Exception as error_info2:
            i += 1
            error_info3 = 'Error in get_html2 :' + str(error_info2)
            print(error_info3)
            print('[-]Connect retry ' + str(i) + '/' + str(retry_count))
    print('[-]Connect Failed! Please check your Proxy or Network!')
    return 'error', error_info3


def post_html(url: str, query: dict):
    proxy_type = ''
    retry_count = 0
    proxy = ''
    timeout = 0
    try:
        proxy_type, proxy, timeout, retry_count = get_proxy()
    except Exception as error_info:
        error_info = 'Error in post_html1 :' + str(error_info)
        print('Error in post_html1 :' + str(error_info))
        print('[-]Proxy config error! Please check the config.')
    proxies = get_proxies(proxy_type, proxy)
    for i in range(retry_count):
        try:
            result = requests.post(url, data=query, proxies=proxies, timeout=timeout)
            result.encoding = 'utf-8'
            result = result.text
            return 'ok', result
        except Exception as error_info:
            error_info1 = 'Error in post_html2 :' + str(error_info)
            print("[-]Connect retry {}/{}".format(i + 1, retry_count))
    print("[-]Connect Failed! Please check your Proxy or Network!")
    print('Error in post_html2:' + error_info1)
    return 'error', error_info1
