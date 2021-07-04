#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from lxml import etree
import json
from Function.getHtml import get_html


def getTitle(a):
    html = etree.fromstring(a, etree.HTMLParser())
    result = str(html.xpath("//span[@id='program_detail_title']/text()")).strip(" ['']").replace("'", '')
    return result


def getActor(a):  # //*[@id="center_column"]/div[2]/div[1]/div/table/tbody/tr[1]/td/text()
    html = etree.fromstring(a, etree.HTMLParser())
    result = str(html.xpath("//li[@class='credit-links']/a/text()")).strip(" ['']").replace("'", '')
    return result


def getActorPhoto(actor):  # //*[@id="star_qdt"]/li/a/img
    actor = actor.split(',')
    d = {}
    for i in actor:
        if ',' not in i:
            p = {i: ''}
            d.update(p)
    return d


def getStudio(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//span[@id='program_detail_maker_name']/text()")).strip(" ['']")
    return result


def getRuntime(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result = str(html.xpath("//span[contains(text(),'収録時間')]/parent::li/text()"))
        if re.search(r'\d+', result):
            result = re.findall(r'\d+', result)[0].replace('/', '-')
    except:
        result = ''
    return result


def getSeries(a):
    html = etree.fromstring(a, etree.HTMLParser())
    result = str(html.xpath("//span[contains(text(),'シリーズ')]/following-sibling::a/span/text()")).strip(" ['']").replace('\'', '')
    return result


def getNum(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//span[@id='hinban']/text()")).strip(" ['']")
    return result


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getRelease(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result = str(html.xpath("//span[contains(text(),'発売日')]/parent::li/text()"))
        if re.search(r'\d{4}/\d{2}/\d{2}', result):
            result = re.findall(r'\d{4}/\d{2}/\d{2}', result)[0].replace('/', '-')
    except:
        result = ''
    return result


def getTag(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath("//a[@class='genre']/text()")).strip(" ['']").replace('\'', '').replace('\\t', '').replace('\\n', '')
    return result1.replace("', '", ",")


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = 'https:' + str(html.xpath("//div[@class='photo']/p[@class='tn']/a/@href")).strip(" ['']").replace('\'', '')
    return result


def getExtraFanart(htmlcode):  # 获取封面链接
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    old_list = html.xpath("//div[@id='sample_images']/div/a/@href")
    new_list = []
    for extrafanart in old_list:
        new_list.append('https:' + extrafanart.replace('scene/small/', ''))
    return new_list


def getDirector(a):
    html = etree.fromstring(a, etree.HTMLParser())
    result1 = str(html.xpath("//span[@id='program_detail_director']/text()")).strip(" ['']").replace('\\t', '').replace('\\n', '')
    return result1


def getOutline(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath("//p[@class='lead']/text()")).strip(" ['']").replace('\\n', '').replace('\n', '')
    return result


def getScore(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath("//p[@class='d-review__average']/strong/text()")[0]).replace('\\n', '').replace('\n', '').replace('点', '')
    return result


def find_number(number, appoint_url):
    if appoint_url:
        return appoint_url, get_html(appoint_url)[1]
    result, htmlcode = get_html('https://xcity.jp/result_published/?q=' + number.replace('-', ''))
    if '該当する作品はみつかりませんでした' in htmlcode:
        return 'Movie data not found', ''
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    counts = len(html.xpath("//div[@id='searchResult']/table[@class='resultList']/tr"))
    if counts >= 2:
        for count in range(2, counts + 1):  # 遍历搜索结果，找到需要的番号
            result_url = 'https://xcity.jp' + html.xpath("//div[@id='searchResult']/table[@class='resultList']/tr[" + str(count) + "]/td[1]/a/@href")[0]
            result, detail_page = get_html(result_url)
            detail_page_html = etree.fromstring(detail_page, etree.HTMLParser())
            number_get = str(detail_page_html.xpath("//span[@id='hinban']/text()")[0])
            if number_get.upper() == number.replace('-', '').upper():
                return result_url, detail_page
    return 'Movie data not found', ''


def main(number, appoint_url='', log_info=''):
    log_info += '   >>> XCITY-开始使用 xcity 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    dic = {}
    try:
        url, detail_page = find_number(number, appoint_url)
        if url == 'Movie data not found':
            log_info += '   >>> XCITY-未匹配到番号！ \n'
            error_type = 'Movie data not found'
            raise Exception('Movie data not found')
        actor = getActor(detail_page)
        release = getRelease(detail_page)
        title = getTitle(detail_page) # 获取标题
        if not title:
            log_info += '   >>> XCITY- title 获取失败！ \n'
            error_type = 'need login'
            raise Exception('>>> XCITY- title 获取失败！]')
        cover_url = getCover(detail_page) # 获取cover
        if 'http' not in cover_url:
            log_info += '   >>> XCITY- cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('>>> XCITY- cover url 获取失败！]')
        studio = getStudio(detail_page)
        try:
            dic = {
                'title': str(title),
                'number': getNum(detail_page),
                'actor': actor,
                'outline': getOutline(detail_page),
                'tag': getTag(detail_page),
                'release': release,
                'year': getYear(release),
                'runtime': getRuntime(detail_page),
                'score': '',
                'series': getSeries(detail_page),
                'director': getDirector(detail_page),
                'studio': studio,
                'publisher': studio,
                'source': 'xcity.main',
                'website': url,
                'actor_photo': getActorPhoto(actor),
                'cover': str(cover_url),
                'cover_small': '',
                'extrafanart': getExtraFanart(detail_page),
                'imagecut': 1,
            }
            log_info += '   >>> XCITY-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
                log_info += '   >>> XCITY-生成数据字典：出错！ 错误信息：%s\n' % str(error_info)
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
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))  # .encode('UTF-8')
    return js


'''
print(main('xc-1280'))
print(main('xv-163'))
print(main('sea-081'))
print(main('IA-28'))
print(main('xc-1298'))
print(main('DMOW185'))
print(main('EMOT007'))
'''
# print(main('EMOT007', "https://xcity.jp/avod/detail/?id=147036"))
