import re
from lxml import etree
import json
import cloudscraper
from Function.getHtml import get_proxies, get_proxy
from configparser import RawConfigParser
import urllib3
urllib3.disable_warnings()


def getRealUrl(html, number, domain_2):
    new_number = number.strip().replace('-', '').upper() + ''
    result = html.xpath('//div[@id="video_title"]/h3/a/text()')
    for each in result:
        if new_number in each.replace('-', '').upper():
            real_url = html.xpath('//div[@id="video_title"]/h3/a[contains(text(), $title)]/@href', title=each)[0]
            real_url = 'https://www.javlibrary.com' + real_url
            return real_url
    result = html.xpath('//a[contains(@href, "/?v=javli")]/@title')
    for each in result:
        if new_number in each.replace('-', '').upper():
            real_url = html.xpath('//a[contains(@title, $title)]/@href', title=each)[0]
            real_url = domain_2 + real_url[1:]
            return real_url      

def getDelActorName():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    del_actor_name = config.getint('Name_Rule', 'del_actor_name')
    return del_actor_name

def getTitle(html):
    result = html.xpath('//div[@id="video_title"]/h3/a/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getNumber(html):
    result = html.xpath('//div[@id="video_id"]/table/tr/td[@class="text"]/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getActor(html):
    result = html.xpath('//div[@id="video_cast"]/table/tr/td[@class="text"]/span/span[@class="star"]/a/text()')
    if result:
        result = str(result).strip(' []').replace("'", '').replace(', ', ',')
    else:
        result = ''
    return result

def getActorPhoto(actor): 
    actor_photo = {}
    if actor:
        actor_list = actor.split(',')
        for each in actor_list:
            actor_photo[each] = ''
    return actor_photo

def getCover(html):
    result = html.xpath("//img[@id='video_jacket_img']/@src")
    if result:
        result = 'https:' + result[0]
    else:
        result = ''
    return result

def getTag(html):
    result = html.xpath('//div[@id="video_genres"]/table/tr/td[@class="text"]/span/a/text()')
    if result:
        result = str(result).strip(' []').replace("'", '').replace(', ', ',')
    else:
        result = ''
    return result

def getRelease(html):
    result = html.xpath('//div[@id="video_date"]/table/tr/td[@class="text"]/text()')
    if result:
        result = str(result).strip(' []').replace("'", '').replace(', ', ',')
    else:
        result = ''
    return result

def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release[:4]

def getStudio(html):
    result = html.xpath('//div[@id="video_maker"]/table/tr/td[@class="text"]/span/a/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getPublisher(html):
    result = html.xpath('//div[@id="video_label"]/table/tr/td[@class="text"]/span/a/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getRuntime(html):
    result = html.xpath('//div[@id="video_length"]/table/tr/td/span[@class="text"]/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getScore(html):
    result = html.xpath('//div[@id="video_review"]/table/tr/td/span[@class="score"]/text()')
    if result:
        result = result[0].strip('()')
    else:
        result = ''
    return result

def getDirector(html):
    result = html.xpath('//div[@id="video_director"]/table/tr/td[@class="text"]/span/a/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def main(number, appoint_url='', translate_language='zh_cn', log_info='', req_web='', isuncensored=False):
    req_web += '-> javlibrary[%s] ' % translate_language.replace('zh_', '')
    log_info += '   >>> javlibrary-开始使用javlibrary 进行刮削\n'
    proxies = get_proxies()
    proxy_type, proxy, timeout, retry_count = get_proxy()
    domain = 'https://www.javlibrary.com'
    real_url = appoint_url
    title = ''
    cover_url = ''
    error_type = ''
    error_info = ''
    url_search = ''
    if translate_language == 'zh_cn':
        javlibrary_url = domain + '/cn/vl_searchbyid.php?keyword='
        domain_2 = 'https://www.javlibrary.com/cn'
    elif translate_language == 'zh_tw':
        javlibrary_url = domain + '/tw/vl_searchbyid.php?keyword='
        domain_2 = 'https://www.javlibrary.com/tw'
    else:
        javlibrary_url = domain + '/ja/vl_searchbyid.php?keyword='
        domain_2 = 'https://www.javlibrary.com/ja'
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        }
    ) 
    try: # 捕获主动抛出的异常
        if not real_url:
            # 通过搜索获取real_url
            url_search = javlibrary_url + number
            log_info += '   >>> javlibrary-生成搜索页地址: %s\n' % url_search
            try:
                html_search = scraper.get(url_search, proxies=proxies, timeout=timeout).text
            except Exception as error_info:
                log_info += '   >>> javlibrary-请求搜索页：出错！错误信息：%s\n' % str(error_info)
                error_type = 'timeout'
                raise Exception('javlibrary-请求搜索页：出错！错误信息：%s\n' % str(error_info))
            html = etree.fromstring(html_search, etree.HTMLParser())
            html_title = str(html.xpath('//title/text()')).strip(" ['']")
            if 'Cloudflare' in html_title:
                real_url = ''
                log_info += '   >>> javlibrary-请求搜索页：被 5 秒盾拦截！\n'
                error_type = 'SearchCloudFlare'
                raise Exception('javlibrary-请求搜索页：被 5 秒盾拦截！')
            real_url = getRealUrl(html, number, domain_2)
            if not real_url:
                log_info += '   >>> javlibrary-搜索结果页：未匹配到番号！\n'
                error_type = 'Movie data not found'
                raise Exception('javlibrary-搜索结果页：未匹配到番号')
            else:
                log_info += '   >>> javlibrary-生成详情页地址：%s\n' % real_url

        if real_url:
            try:
                html_info = scraper.get(real_url, proxies=proxies, timeout=timeout).text
            except Exception as error_info:
                log_info += '   >>> javlibrary-请求详情页：出错！错误信息：%s\n' % str(error_info)
                error_type = 'timeout'
                raise Exception('javlibrary-请求详情页：出错！错误信息：%s\n' % str(error_info))
            html_detail = etree.fromstring(html_info, etree.HTMLParser())
            html_title = str(html_detail.xpath('//title/text()')).strip(" ['']")
            if html_title == 'Please Wait... | Cloudflare':
                log_info += '   >>> javlibrary-请求详情页：被 5 秒盾拦截！\n'
                error_type = 'SearchCloudFlare'
                raise Exception('javlibrary-请求详情页：被 5 秒盾拦截！')
            title = getTitle(html_detail)
            if not title:
                log_info += '   >>> javlibrary-title 获取失败！\n'
                error_type = 'title 获取失败'
                raise Exception('javlibrary-title 获取失败！')
            web_number = getNumber(html_detail)
            title = title.strip(web_number + ' ')   # 去掉标题里的番号
            actor = getActor(html_detail) # 获取actor
            actor_photo = getActorPhoto(actor)
            if getDelActorName():
                title = title.strip(' ' + actor)
            cover_url = getCover(html_detail) # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> javlibrary-cover url 获取失败！\n'
                error_type = 'Cover Url is None!'
                raise Exception('javlibrary-cover url 获取失败！')
            tag =  getTag(html_detail)
            release = getRelease(html_detail)
            year = getYear(release)
            studio = getStudio(html_detail)
            publisher = getPublisher(html_detail)
            runtime = getRuntime(html_detail)
            score = getScore(html_detail)
            director = getDirector(html_detail)

            try:
                dic = {
                    'title': title,
                    'number': web_number,
                    'actor': actor,
                    'outline': '',
                    'tag': tag,
                    'release': release,
                    'year': year,
                    'runtime': runtime,
                    'score': score,
                    'series': '',
                    'director': director,
                    'studio': studio,
                    'publisher': publisher,
                    'source': 'javlibrary',
                    'website': real_url,
                    'search_url': url_search,
                    'actor_photo': actor_photo,
                    'cover': cover_url,
                    'cover_small': '',
                    'extrafanart': '',
                    'imagecut': 1,
                    'log_info': str(log_info),
                    'error_type': '',
                    'error_info': str(error_info),
                    'req_web': req_web,
                }
                log_info += '   >>> javlibrary-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> javlibrary-生成数据字典：出错！ 错误信息：%s\n' % str(error_info)
                error_info = str(error_info)
                raise Exception(log_info)

    except Exception as error_info:
        dic = {
            'title': '',
            'cover': '',
            'website': str(real_url).strip('[]'),
            'log_info': str(log_info),
            'error_type': str(error_type),
            'error_info': str(error_info),
            'req_web': req_web,
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js



# print(main(' IPX-071'))
# print(main('SNIS-003'))
# print(main('SSIS-118'))
# print(main('AA-007'))
# print(main('abs-141'))
# print(main('HYSD-00083'))
# print(main('IESP-660'))
# print(main('n1403'))
# print(main('GANA-1910'))
# print(main('heyzo-1031'))
# print(main_us('x-art.19.11.03'))
# print(main('032020-001'))
# print(main('S2M-055'))
# print(main('LUXU-1217'))
# print(main('SSIS-001', ''))
# print(main('SSIS-090', ''))
# print(main('SNIS-016', ''))
# print(main('HYSD-00083', ''))
# print(main('IESP-660', ''))
# print(main('n1403', ''))
# print(main('GANA-1910', ''))
# print(main('heyzo-1031', ''))
# print(main_us('x-art.19.11.03'))
# print(main('032020-001', ''))
# print(main('S2M-055', ''))
# print(main('LUXU-1217', ''))
# print(main_us('x-art.19.11.03', ''))
