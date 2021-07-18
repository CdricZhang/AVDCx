import re
from lxml import etree
import json
from Function.getHtml import get_html
import urllib3
urllib3.disable_warnings()

def getTitle(html):  # 获取标题
    result = html.xpath('//h3/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getCover(html):  # 获取封面
    extrafanart = html.xpath('//ul[@class="items_article_SampleImagesArea"]/li/a/@href')
    if extrafanart:
        result = extrafanart[0]
    else:
        result = ''
    return result, extrafanart

def getCoverSmall(html):  # 获取小图
    result = html.xpath('//div[@class="items_article_MainitemThumb"]/span/img/@src')
    if result:
        result = 'https:' + result[0]
    else:
        result = ''
    return result

def getRelease(html):
    result = html.xpath('//div[@class="items_article_Releasedate"]/p/text()')
    result = re.findall('\d+/\d+/\d+', str(result))
    if result:
        result = result[0].replace('/', '-')
    else:
        result = ''
    return result

def getStudio(html):  # 使用卖家作为厂家
    result = html.xpath('//div[@class="items_article_headerInfo"]/ul/li[last()]/a/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result

def getTag(html):  # 获取标签
    result = html.xpath('//a[@class="tag tagTag"]/text()')
    result = str(result).strip(" ['']").replace("', '", ",")
    return result


def getOutline(html):  # 获取简介
    result = html.xpath('//meta[@name="description"]/@content')
    if result:
        result = result[0]
    else:
        result = ''
    return result


def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> fc2 '
    log_info += '   >>> FC2.COM-开始使用 FC2.COM 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small_url = ''
    error_type = ''
    error_info = ''
    number = number.upper().replace('FC2PPV', '').replace('FC2-PPV-', '').replace('FC2-', '').replace('-', '').strip()
    dic = {}
    try: # 捕获主动抛出的异常
        if not real_url:
            # 通过搜索获取real_url
            real_url = 'https://adult.contents.fc2.com/article/%s/' % number
        log_info += '   >>> FC2.COM-请求详情页地址: %s \n' % real_url
        # ========================================================================搜索番号
        result, html_content = get_html(real_url)
        # with open('11.txt', 'wt') as f:
        #     f.write(html_content)
        if not result:
            log_info += '   >>> FC2.COM-请求详情页：错误！信息：%s\n' % html_content
            error_type = 'request erro'
            raise Exception('FC2.COM-请求详情页：错误！信息：' + html_content)
        html_info = etree.fromstring(html_content, etree.HTMLParser())

        title = getTitle(html_info) # 获取标题
        if 'お探しの商品が見つかりません' in title:
            log_info += '   >>> FC2.COM-找不到该番号数据！\n'
            error_type = '找不到该番号数据'
            raise Exception('FC2.COM-找不到该番号数据！')

        cover_url, extrafanart = getCover(html_info) # 获取cover,extrafanart
        if 'http' not in cover_url:
            log_info += '   >>> FC2.COM-cover url is none!\n'
            error_type = 'Cover Url is None!'
            raise Exception('FC2.COM-cover url is none!')

        cover_small_url = getCoverSmall(html_info)
        outline = getOutline(html_info)
        tag = getTag(html_info)
        release = getRelease(html_info)
        studio = getStudio(html_info) # 使用卖家作为厂商
        try:
            dic = {
                'title': title,
                'number': 'FC2-' + str(number),
                'actor': 'FC2系列',
                'outline': outline,
                'tag': tag,
                'release': release,
                'year': release[:4],
                'runtime': '',
                'score': '',
                'series': 'FC2系列',
                'director': '',
                'studio': studio,
                'publisher': studio,
                'source': 'fc2.main',
                'website': real_url,
                'actor_photo': {'FC2系列':''},
                'cover': cover_url,
                'cover_small': cover_small_url,
                'extrafanart': extrafanart,
                'imagecut': 0,
                'msaico': '无码',
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
                'req_web': req_web,
            }
            log_info += '   >>> FC2.COM-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
            log_info += '   >>> FC2.COM-生成数据字典：出错！ 错误信息：%s \n' % str(error_info)
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
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'), )
    return js


# print(main('1723984', ''))
# print(main('1924776', ''))
# print(main('1860858', ''))
# print(main('1599412', ''))    # fc2hub有，fc2/fc2club没有
# print(main('1131214', ''))    # fc2club有，fc2/fc2hub没有
# print(main('1837553', ''))
# print(main('1613618', ''))
# print(main('1837553', ''))
# print(main('1837589', ""))
# print(main('1760182', ''))
# print(main('1251689', ''))
# print(main('674239', ""))
# print(main('674239', "))
