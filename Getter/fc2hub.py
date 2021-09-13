import re
from lxml import etree
import json
from Function.getHtml import get_html
import urllib3
urllib3.disable_warnings()

def getTitle(html):  # 获取标题
    result = html.xpath('//h1/text()')
    if result:
        result = result[1]
    else:
        result = ''
    return result


def getNum(html):  # 获取番号
    result = html.xpath('//h1/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result


def getCover(html):  # 获取封面
    result = html.xpath('//a[@data-fancybox="gallery"]/@href')
    if result:
        result = result[0]
    else:
        result = ''
    return result


def getExtraFanart(html):  # 获取剧照
    result = html.xpath('//div[@style="padding: 0"]/a/@href')
    return result

def getStudio(html):  # 使用卖家作为厂家
    result = html.xpath('//div[@class="col-8"]/text()')
    if result:
        result = result[0].strip()
    return result

def getTag(html):  # 获取标签
    result = html.xpath('//p[@class="card-text"]/a[contains(@href, "/tag/")]/text()')
    if result:
        result = str(result).strip(' ['']').replace(", ", ',').replace("'", '').strip()
    else:
        result = ''
    return result

def getOutline(html):  # 获取简介
    result = str(html.xpath('//div[@class="col des"]/text()')).strip('['']').replace("',", '').replace('\\n', '').replace("'", '').replace('・', '').strip()
    return result

def getMosaic(tag, title):  # 获取马赛克
    if '無修正' in tag or '無修正' in title:
        result = '无码'
    else:
        result = '有码'
    return result

def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> fc2hub '
    log_info += '   >>> FC2HUB-开始使用 fc2hub 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    number = number.upper().replace('FC2PPV', '').replace('FC2-PPV-', '').replace('FC2-', '').replace('-', '').strip()
    dic = {}
    try: # 捕获主动抛出的异常
        if not real_url:
            # 通过搜索获取real_url
            url_search = 'https://fc2hub.com/search?kw=' + number
            log_info += '   >>> FC2HUB-生成搜索页地址: %s \n' % url_search
            # ========================================================================搜索番号
            result, html_search = get_html(url_search)
            if not result:
                log_info += '   >>> FC2HUB-请求搜索页：错误！信息：%s\n' % html_search
                error_type = 'timeout'
                raise Exception('>>> FC2HUB-请求搜索页：错误！信息：' + html_search)
            # with open('11.txt', 'wt') as f:
            #     f.write(web_cache_url)
            html = etree.fromstring(html_search, etree.HTMLParser())
            real_url = html.xpath("//link[contains(@href, $number)]/@href", number='id' + number)

            if not real_url:
                log_info += '   >>> FC2HUB-搜索结果页匹配番号：未匹配到番号！ \n'
                error_type = 'Movie data not found'
                raise Exception('FC2HUB-搜索结果页匹配番号：未匹配到番号！')
            else:
                real_url = real_url[0]
                real_url = real_url.replace(('/' + real_url.split('/')[-1]), '')
                log_info += '   >>> FC2HUB-匹配详情页地址： %s \n' % real_url
        if real_url:
            try:
                result, html_content = get_html(real_url)
            except Exception as error_info:
                log_info += '   >>> FC2HUB-请求详情页：出错！错误信息：%s \n' % str(error_info)
                error_type = 'timeout'
                raise Exception('>>> FC2HUB-请求详情页：出错！错误信息：%s \n' % str(error_info))          
            html_info = etree.fromstring(html_content, etree.HTMLParser())

            title = getTitle(html_info) # 获取标题
            if not title:
                log_info += '   >>> FC2HUB- title 获取失败！ \n'
                error_type = 'need login'
                raise Exception('>>> FC2HUB- title 获取失败!')
            cover_url = getCover(html_info) # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> FC2HUB-Cover Url is None! \n'
                error_type = 'Cover Url is None!'
                raise Exception('FC2HUB-Cover Url is None!')
            outline = getOutline(html_info)
            tag = getTag(html_info)
            studio = getStudio(html_info) # 获取厂商
            extrafanart = getExtraFanart(html_info)
            mosaic = getMosaic(tag, title)

            try:
                dic = {
                    'title': str(title),
                    'number': 'FC2-' + str(number),
                    'actor': studio,
                    'outline': outline,
                    'tag': tag,
                    'release': '',
                    'year': '',
                    'runtime': '',
                    'score': '',
                    'series': 'FC2系列',
                    'director': '',
                    'studio': studio,
                    'publisher': studio,
                    'source': 'fc2hub.main',
                    'website': str(real_url).strip('[]'),
                    'actor_photo': {studio:''},
                    'cover': str(cover_url),
                    'cover_small': '',
                    'extrafanart': extrafanart,
                    'image_download': False,
                    'image_cut': 'center',
                    'mosaic': mosaic,
                    'log_info': str(log_info),
                    'error_type': '',
                    'error_info': str(error_info),
                    'req_web': req_web,
                }
                log_info += '   >>> FC2HUB-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> FC2HUB-生成数据字典：出错！ 错误信息：%s \n' % str(error_info)
                error_info = str(error_info)
                raise Exception(log_info)        
    except Exception as error_info:
        dic = {
            'title': '',
            'cover': '',
            'website': str(real_url),
            'log_info': str(log_info),
            'error_type': str(error_type),
            'error_info': str(error_info),
            'req_web': req_web,
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'), )
    return js



# print(main('1940476'))  # 无码
# print(main('1860858', ''))  #有码
# print(main('1599412', ''))
# print(main('1131214', ''))  # 未找到
# print(main('1837553', ''))
# print(main('1613618', ''))
# print(main('1837553', ''))
# print(main('1837589', ""))
# print(main('1760182', ''))
# print(main('1251689', ''))
# print(main('674239', ""))
# print(main('674239', "))
# print(main('1924003', ''))   # 无图
