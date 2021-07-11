import requests
from configparser import RawConfigParser
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# ========================================================================获取proxy
def get_proxy():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    proxy_type = config.get('proxy', 'type')
    proxy = config.get('proxy', 'proxy')
    timeout = config.getint('proxy', 'timeout') # 单位秒
    retry_count = config.getint('proxy', 'retry')
    return proxy_type, proxy, timeout, retry_count


# ========================================================================获取proxies
def get_proxies():
    proxy_type, proxy, timeout, retry_count = get_proxy()
    proxies = {}
    if proxy_type == 'http':
        proxies = {"http": "http://" + proxy, "https": "http://" + proxy}
    elif proxy_type == 'socks5':
        proxies = {"http": "socks5h://" + proxy, "https": "socks5h://" + proxy}
    return proxies


# ========================================================================获取cookies
def get_cookies(website):
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    dic = {}
    try:
        cookies_value = config.get('Cookies', website)
    except:
        return None
    dic_cookie = {'cookie':cookies_value}
    dic.update(dic_cookie)
    return dic


# ========================================================================网页请求
def get_html(url, cookies=None):
    proxy_type, proxy, timeout, retry_count = get_proxy()
    proxies = get_proxies()
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
    proxy_type, proxy, timeout, retry_count = get_proxy()

    proxies = get_proxies()
    for i in range(retry_count):
        try:
            result = requests.post(url=url, data=query, headers=headers,proxies=proxies, timeout=timeout)
            result.encoding = 'utf-8'
            result = result.text
            return 'ok', result
        except Exception as error_info:
            error_info1 = 'Error in post_html2 :' + str(error_info)
            print("[-]Connect retry {}/{}".format(i + 1, retry_count))
    print("[-]Connect Failed! Please check your Proxy or Network!")
    print('Error in post_html2:' + error_info1)
    return 'error', error_info1
