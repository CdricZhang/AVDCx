import re
from lxml import etree
import json
from Function.getHtml import get_html


def getTitle(htmlcode):
    try:
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result = str(html.xpath('//*[@id="center_column"]/div[1]/h1/text()')).strip(" ['']")
        return result.replace('/', ',')
    except:
        return ''


def getActor(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"出演")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"出演")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('/', ',').replace('\'', '').replace(' ', '').replace('\\n', '')


def getActorPhoto(actor):
    d = {}
    for i in actor:
        if ',' not in i or ')' in i:
            p = {i: ''}
            d.update(p)
    return d


def getStudio(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getPublisher(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getRuntime(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).rstrip('min').replace('\'', '').replace(' ', '').replace('\\n', '')


def getSeries(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getNum(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"品番：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"品番：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getRelease(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getTag(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//*[@id="center_column"]/div[1]/div[1]/div/div/h2/img/@src')).strip(" ['']")
    return result


def getExtraFanart(htmlcode):  # 获取封面链接
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    extrafanart_list = html.xpath("//dl[@id='sample-photo']/dd/ul/li/a[@class='sample_image']/@href")
    return extrafanart_list


def getOutline(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//*[@id="introduction"]/dd/p[1]/text()')).strip(" ['']")
    return result


def getScore(htmlcode):
    return str(re.findall(r'5点満点中 (\S+)点', htmlcode)).strip(" ['']")


def main(number, appoint_url='', log_info=''):
    log_info += '   >>> MGSTAGE-开始使用 mgstage 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    dic = {}

    try:
        number = number.upper()
        url = 'https://www.mgstage.com/product/product_detail/' + str(number) + '/'
        if appoint_url != '':
            url = appoint_url
        result, htmlcode = str(get_html(url, cookies={'adc': '1'}))
        htmlcode = htmlcode.replace('ahref', 'a href')  # 针对a标签、属性中间未分开
        if not result:
            log_info += '   >>> MGSTAGE-请求详情页：错误！信息：' + htmlcode
            error_type = 'timeout'
            raise Exception('>>> MGSTAGE-请求详情页：错误！信息：' + htmlcode)

        title = getTitle(htmlcode).replace("\\n", '').replace('        ', '').strip(',') # 获取标题
        if not title:
            log_info += '   >>> MGSTAGE- title 获取失败！ \n'
            error_type = 'need login'
            raise Exception('>>> MGSTAGE- title 获取失败！]')
        cover_url = getCover(htmlcode).strip(',') # 获取cover
        if 'http' not in cover_url:
            log_info += '   >>> MGSTAGE- cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('>>> MGSTAGE- cover url 获取失败！]')

        actor = getActor(htmlcode).replace(' ', '')
        release = getRelease(htmlcode)
        try:
            dic = {
                'title': str(title),
                'number': getNum(htmlcode).strip(','),
                'actor': actor.strip(','),
                'outline': getOutline(htmlcode).replace('\n', '').strip(','),
                'tag': getTag(htmlcode).strip(','),
                'release': release.strip(',').replace('/', '-'),
                'year': getYear(release).strip(','),
                'runtime': getRuntime(htmlcode).strip(','),
                'score': getScore(htmlcode).strip(','),
                'series': getSeries(htmlcode).strip(','),
                'director': '',
                'studio': getStudio(htmlcode).strip(','),
                'publisher': getPublisher(htmlcode).strip(','),
                'source': 'mgstage.main',
                'website': url,
                'actor_photo': getActorPhoto(actor.split(',')),
                'cover': str(cover_url),
                'cover_small': '',
                'extrafanart': getExtraFanart(htmlcode),
                'imagecut': 0,
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
            }

            log_info += '   >>> MGSTAGE-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
            log_info += '   >>> MGSTAGE-生成数据字典：出错！ 错误信息：%s\n' % str(error_info)
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
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js
'''
print(main('200GANA-2240'))
print(main('SIRO-4042'))
print(main('300MIUM-382'))
'''
# print(main('300MIUM-382', ''))
# print(main('300MIUM-382', 'https://www.mgstage.com/product/product_detail/300MIUM-382/'))
