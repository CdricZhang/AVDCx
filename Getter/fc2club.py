import re
from lxml import etree
import json
from Function.getHtml import get_html
import urllib3
urllib3.disable_warnings()

def getTitle(html, number):  # 获取标题
    result = html.xpath('//h3/text()')
    if result:
        result = result[0].replace(('FC2-%s ' % number), '')
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
    extrafanart = []
    result = html.xpath('//img[@class="responsive"]/@src')
    if result:
        for res in result:
            extrafanart.append(res.replace('../uploadfile', 'https://fc2club.net/uploadfile'))
        result = result[0].replace('../uploadfile', 'https://fc2club.net/uploadfile')
    else:
        result = ''
    return result, extrafanart

def getStudio(html):  # 使用卖家作为厂家
    result = html.xpath('//strong[contains(text(), "卖家信息")]/../a/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result

def getScore(html):  # 获取评分
    try:
        result = html.xpath('//strong[contains(text(), "影片评分")]/../text()')
        result = re.findall('\d+', result[0])[0]
    except:
        result = ''
    return result

def getActor(html, studio):  # 获取演员
    result = html.xpath('//strong[contains(text(), "女优名字")]/../a/text()')
    if result:
        result = str(result).strip(' []').replace('"', '').replace("'", '').replace(', ', ',')
    else:
        result = studio
    return result

def getActorPhoto(actor):  # 获取演员头像
    actor_photo = {}
    actor_list = actor.split(',')
    for act in actor_list: 
        actor_photo[act] = ''
    return actor_photo

def getTag(html):  # 获取标签
    result = html.xpath('//strong[contains(text(), "影片标签")]/../a/text()')
    result = str(result).strip(' []').replace('"', '').replace("'", '').replace(', ', ',')
    return result

def getOutline(html):  # 获取简介
    result = str(html.xpath('//div[@class="col des"]/text()')).strip('['']').replace("',", '').replace('\\n', '').replace("'", '').replace('・', '').strip()
    return result

def getMosaic(html):  # 获取马赛克
    result = str(html.xpath('//h5/strong[contains(text(), "资源参数")]/../text()'))
    if '无码' in result:
        mosaic = '无码'
    else:
        mosaic = '有码'
    return mosaic

def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> fc2club '
    log_info += '   >>> FC2CLUB-开始使用 FC2CLUB 进行刮削\n'
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
            real_url = 'https://fc2club.net/html/FC2-%s.html' % number

        log_info += '   >>> FC2CLUB-请求详情页地址: %s \n' % real_url
        # ========================================================================搜索番号
        result, html_content = get_html(real_url)
        # with open('11.txt', 'wt') as f:
        #     f.write(html_content)
        if not result:
            log_info += '   >>> FC2CLUB-请求详情页：错误！信息：%s\n' % html_content
            error_type = 'request erro'
            raise Exception('FC2CLUB-请求详情页：错误！信息：' + html_content)
        html_info = etree.fromstring(html_content, etree.HTMLParser())

        title = getTitle(html_info, number) # 获取标题
        if not title:
            log_info += '   >>> FC2CLUB-404 Not Found！ \n'
            error_type = '404 Not Found'
            raise Exception('FC2CLUB-404 Not Found')

        cover_url, extrafanart = getCover(html_info) # 获取cover
        if 'http' not in cover_url:
            log_info += '   >>> FC2CLUB-cover url is none!\n'
            error_type = 'Cover Url is None!'
            raise Exception('>>> FC2CLUB-cover url is none!')

        # outline = getOutline(html_info)
        tag = getTag(html_info)
        studio = getStudio(html_info) # 获取厂商
        score = getScore(html_info) # 获取厂商
        actor = getActor(html_info, studio) # 获取演员
        actor_photo = getActorPhoto(actor)  # 获取演员列表
        mosaic = getMosaic(html_info)
        try:
            dic = {
                'title': str(title),
                'number': 'FC2-' + str(number),
                'actor': actor,
                'outline': '',
                'tag': tag,
                'release': '',
                'year': '',
                'runtime': '',
                'score': score,
                'series': 'FC2系列',
                'director': '',
                'studio': studio,
                'publisher': studio,
                'source': 'fc2club.main',
                'website': str(real_url).strip('[]'),
                'actor_photo': actor_photo,
                'cover': cover_url,
                'cover_small': '',
                'extrafanart': extrafanart,
                'imagecut': 0,
                'mosaic': mosaic,
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
                'req_web': req_web,
            }
            log_info += '   >>> FC2CLUB-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
            log_info += '   >>> FC2CLUB-生成数据字典：出错！ 错误信息：%s \n' % str(error_info)
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



# print(main('1470588', ''))
# print(main('674261', ''))
# print(main('406570', ''))
# print(main('1474843', ''))
# print(main('1860858', ''))
# print(main('1599412', ''))
# print(main('1131214', ''))
# print(main('1837553', ''))
# print(main('1613618', ''))
# print(main('1837553', ''))
# print(main('1837589', ""))
# print(main('1760182', ''))
# print(main('1251689', ''))
# print(main('674239', ""))
# print(main('674239', "))
