#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')  # NOQA: E402
import re
from lxml import etree
import json
from Function.getHtml import get_html
import Function.config as cf
import urllib3
urllib3.disable_warnings()


def getTitle(html):
    result = html.xpath('//span[@id="program_detail_title"]/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result


def getWebNumber(html):
    result = html.xpath('//span[@id="hinban"]/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result


def getActor(html):
    try:
        result = str(html.xpath(
            '//li[@class="credit-links"]/a/text()')).strip("['']").replace("'", '')
    except:
        result = ''
    return result


def getActorPhoto(actor):
    actor = actor.split(',')
    d = {}
    for i in actor:
        if ',' not in i:
            p = {i: ''}
            d.update(p)
    return d


def getCover(html):
    result = html.xpath('//div[@class="photo"]/p/a/@href')
    if result:
        result = 'https:' + result[0]
    else:
        result = ''
    return result


def getOutline(html):
    result = html.xpath('//p[@class="lead"]/text()')
    if result:
        result = result[0].strip().replace('"', '')
    else:
        result = ''
    return result


def getRelease(html):
    result = html.xpath(
        '//li/span[@class="koumoku" and (contains(text(), "発売日"))]/../text()')
    result = re.findall('[\d]+/[\d]+/[\d]+', str(result))
    if result:
        result = result[0].replace('/', '-')
    else:
        result = ''
    return result


def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release[:4]


def getTag(html):
    result = html.xpath('//a[@class="genre"]/text()')
    if result:
        result = str(result).strip(" ['']").replace("'", "").replace(
            ', ', ',').replace('\\n', '').replace('\\t', '')
    else:
        result = ''
    return result


def getStudio(html):
    result = html.xpath('//span[@id="program_detail_maker_name"]/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result


def getPublisher(html):
    result = html.xpath('//span[@id="program_detail_label_name"]/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result


def getRuntime(html):
    result = str(html.xpath(
        '//span[@class="koumoku"][contains(text(), "収録時間")]/../text()'))
    result = re.findall('[\d]+', result)
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result


def getDirector(html):
    result = html.xpath('//span[@id="program_detail_director"]/text()')
    if result:
        result = result[0].replace('\\n', '').replace('\\t', '').strip()
    else:
        result = ''
    return result


def getExtrafanart(html):
    result = html.xpath('//a[contains(@class, "thumb")]/@href')
    if result:
        result = str(result).replace('//faws.xcity.jp/scene/small/',
                                     'https://faws.xcity.jp/').strip(' []').replace("'", '').replace(', ', ',')
        result = result.split(',')
    else:
        result = ''
    return result


def getCoverSmall(html):
    result = html.xpath('//img[@class="packageThumb"]/@src')
    if result:
        result = 'https:' + result[0]
    else:
        result = ''
    return result.replace('package/medium/', '')


def getSeries(html):
    result = html.xpath('//a[contains(@href, "series")]/span/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result


def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> xcity '
    log_info += '   >>> xcity-开始使用 xcity 进行刮削\n'
    config = cf.get_config()
    del_actor_name = config.get('del_actor_name')
    real_url = appoint_url
    cover_url = ''
    cover_small_url = ''
    image_download = False
    image_cut = 'right'
    error_type = ''
    error_info = ''
    dic = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'referer': 'https://xcity.jp/result_published/?genre=%2Fresult_published%2F&q=2&sg=main&num=60',
    }

    try:
        if not real_url:
            url_search = 'https://xcity.jp/result_published/?q=' + \
                number.replace('-', '')
            log_info += '   >>> xcity-生成搜索页地址: %s \n' % url_search
        result, html_search = get_html(url_search, headers=headers)
        # getweb = requests.get(url_search, headers=headers, proxies=proxies, verify=False)
        # getweb.encoding = 'utf-8'
        # result, html_search = True, getweb.text
        # with open('124', 'w') as f:
        #     f.write(html_search)
        if not result:
            log_info += '   >>> xcity-请求搜索页：错误！信息：%s\n' % html_search
            error_type = 'timeout'
            raise Exception('>>> xcity-请求搜索页：错误！信息：' + html_search)
        if '該当する作品はみつかりませんでした' in html_search:
            log_info += '   >>> xcity-搜索结果页匹配番号：未匹配到番号！ \n'
            error_type = 'Movie data not found'
            raise Exception('xcity-搜索结果页匹配番号：未匹配到番号！')
        html = etree.fromstring(html_search, etree.HTMLParser())
        # real_url = html.xpath("//p[@class='x-itemBox-title']/a/@href")
        real_url = html.xpath("//table[@class='resultList']/tr/td/a/@href")
        if not real_url:
            log_info += '   >>> xcity-搜索结果页匹配番号：未匹配到番号！ \n'
            error_type = 'Movie data not found'
            raise Exception('xcity-搜索结果页匹配番号：未匹配到番号！')
        else:
            real_url = 'https://xcity.jp' + real_url[0]
            log_info += '   >>> xcity-匹配详情页地址： %s \n' % real_url
        if real_url:
            try:
                result, html_content = get_html(real_url)
            except Exception as error_info:
                log_info += '   >>> xcity-请求详情页：出错！错误信息：%s \n' % str(
                    error_info)
                error_type = 'timeout'
                raise Exception('>>> xcity-请求详情页：出错！错误信息：%s \n' %
                                str(error_info))
            html_info = etree.fromstring(html_content, etree.HTMLParser())

            title = getTitle(html_info)  # 获取标题
            if not title:
                log_info += '   >>> xcity-title 获取失败！ \n'
                error_type = 'xcity-title 获取失败！'
                raise Exception('xcity-title 获取失败!')
            web_number = getWebNumber(html_info)    # 获取番号，用来替换标题里的番号
            title = title.replace(' %s' % web_number, '').strip()
            actor = getActor(html_info)  # 获取actor
            actor_photo = getActorPhoto(actor)
            if del_actor_name:
                title = title.replace(' ' + actor, '')
            cover_url = getCover(html_info)  # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> xcity-cover url 获取失败！ \n'
                error_type = 'Cover Url is None!'
                raise Exception('xcity-cover url 获取失败!')
            outline = getOutline(html_info)
            release = getRelease(html_info)
            year = getYear(release)
            tag = getTag(html_info)
            studio = getStudio(html_info)
            publisher = getPublisher(html_info)
            runtime = getRuntime(html_info)
            director = getDirector(html_info)
            extrafanart = getExtrafanart(html_info)
            cover_small_url = getCoverSmall(html_info)
            score = ''
            series = getSeries(html_info)
            try:
                dic = {
                    'title': title,
                    'number': web_number,
                    'actor': actor,
                    'outline': outline,
                    'tag': tag,
                    'release': release,
                    'year': year,
                    'runtime': runtime,
                    'score': score,
                    'series': series,
                    'director': director,
                    'publisher': publisher,
                    'studio': studio,
                    'source': 'xcity',
                    'website': real_url,
                    'search_url': url_search,
                    'actor_photo': actor_photo,
                    'cover': cover_url,
                    'cover_small': cover_small_url,
                    'extrafanart': extrafanart,
                    'image_download': image_download,
                    'image_cut': image_cut,
                    'log_info': str(log_info),
                    'error_type': '',
                    'error_info': str(error_info),
                    'req_web': req_web,
                    'mosaic': '有码',
                }
                log_info += '   >>> xcity-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> xcity-生成数据字典：出错！ 错误信息：%s\n' % str(
                    error_info)
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
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False,
                    indent=4, separators=(',', ':'))  # .encode('UTF-8')
    return js


if __name__ == '__main__':
    print(main('STVF010'))
    # print(main('MXGS563'))
    # print(main('xc-1280'))
    # print(main('xv-163'))
    # print(main('sea-081'))
    # print(main('IA-28'))
    # print(main('xc-1298'))
    # print(main('DMOW185'))
    # print(main('EMOT007'))
    # print(main('EMOT007', "https://xcity.jp/avod/detail/?id=147036"))
