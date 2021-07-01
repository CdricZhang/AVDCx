#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from lxml import etree
import json
from Function.getHtml import get_html, get_cookies


def getTitle(html):
    result = html.xpath('//img[@class="tdmm"]/@alt')
    if result:
        return result[0]
    return ''


def getActor(html): 
    result = str(html.xpath("//span[@id='performer']/a/text()")).strip(" ['']").replace(
        "', '", ',')
    return result

def getActorPhoto(actor):
    actor = actor.split(',')
    data = {}
    for i in actor:
        actor_photo = {i: ''}
        data.update(actor_photo)
    return data

def getStudio(html):
    result = html.xpath("//a[contains(@href, 'article=maker')]/text()")
    if result:
        return result[0]
    return ''


def getRuntime(html):
    result = html.xpath("//td[contains(text(),'収録時間')]/following-sibling::td/text()")
    if result:
        return re.search('\d+', str(result[0])).group()
    return ''


def getSeries(html):
    result = html.xpath("//td[contains(text(),'シリーズ：')]/following-sibling::td/a/text()")
    if result:
        return result[0]
    return ''


def getNum(html):
    result = html.xpath("//td[contains(text(),'品番：')]/following-sibling::td/text()")
    if result:
        return result[0]
    return ''


def getYear(release):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return release


def getRelease(html):
    result = html.xpath("//td[contains(text(),'発売日：')]/following-sibling::td/text()")
    if result:
        return result[0].lstrip('\n')
    return ''


def getTag(html):
    result = str(html.xpath("//td[contains(text(),'ジャンル：')]/following-sibling::td/a/text()"))
    if result:
        return str(result).strip(" ['']").replace("', '", ",")
    return ''



def getCover(html):
    result = html.xpath('//a[@name="package-image"]/@href')
    if result:
        return result[0]
    return ''


def getExtraFanart(html):
    result = html.xpath("//div[@id='sample-image-block']/a/img/@src")
    if result:
        return result
    return ''


def getDirector(html):
    result = html.xpath("//td[contains(text(),'監督：')]/following-sibling::td/a/text()")
    if result:
        return result[0]
    return ''


def getOutline(html):
    result = html.xpath("//p[@class='mg-b20']/text()")
    if result:
        return result[0].replace('\\n', '').replace('\n', '')
    return ''


def getScore(html):
    result = html.xpath("//p[@class='d-review__average']/strong/text()")
    if result:
        return result[0].replace('\\n', '').replace('\n', '').replace('点', '')
    return ''

def main(number, appoint_url='', log_info=''):
    log_info += '   >>> DMM-开始使用 dmm 进行刮削\n'
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    dic = {}
    new_number = number.lower().replace('-', '')
    url = 'https://www.dmm.co.jp/search/=/searchstr=' + new_number
    num1 = '/cid=' + new_number + '/'
    num2 = new_number + '/'
    cookies = get_cookies()['dmm']
    try:
        if appoint_url: # 如果传入地址，则使用传入的地址
            url = appoint_url
        result, htmlcode = get_html(url, cookies=cookies)
        if result == 'error':
            log_info += '   >>> DMM-请求URL：%s 出现错误：%s' % (url, htmlcode)
            error_type = 'timeout'
            raise Exception('DMM-请求URL：%s 出现错误：%s' % (url, htmlcode))

        if re.findall('foreignError', htmlcode):
            error_info = '   >>> DMM-地域限制, 请使用日本节点访问！'
            log_info += '   >>> DMM-地域限制, 请使用日本节点访问！'
            error_type = 'area blocked'
            raise Exception('DMM-地域限制, 请使用日本节点访问！')

        if re.findall('ageCheck', htmlcode):   # 如果页面有ageCheck，表示无cookie或cookie失效，需要进行年龄认证
            if cookies['Cookie']:
                log_info += '   >>> DMM-Cookie 已失效，请到设置中更新 Cookie！\n'
            else:
                log_info += '   >>> DMM-请到【设置】-【网络设置】中添加 dmm Cookie！\n'
            error_type = 'need cookie'
            raise Exception('DMM-年龄认证拦截，需更新Cookie！')

        html = etree.fromstring(htmlcode, etree.HTMLParser())   # 当前如果是传入的url就是详情页，如果不是传入url，就是搜索页
        if appoint_url:  # 如果是传入的地址，判断页面地址是否正确
            if '404 Not Found' in str(html.xpath("//span[@class='d-txten']/text()")):   # 如果页面有404，表示传入的页面地址不对
                log_info += '   >>> DMM-未匹配到番号' 
                error_type = 'Movie not found'
                raise Exception('DMM-未匹配到番号')
        else:            # 如果不是传入的地址，则上面请求的是搜索页，需要再解析搜索页，获取详情页地址
            if html.xpath("//a[contains(@href, $val)]", val=num1): # 优先匹配'/cid=snis126/'这样链接的，图上面没有蓝光水印
                url = html.xpath("//a[contains(@href, $val)]/@href", val=num1)[0]
            elif html.xpath("//a[contains(@href, 'detail')][contains(@href, $val)]/@href", val=num2): # 如果链接中包含detail和number，则表示找到了
                url = html.xpath("//a[contains(@href, 'detail')][contains(@href, $val)]/@href", val=num2)[0]
            else:
                log_info += '   >>> DMM-未匹配到番号' 
                error_type = 'Movie not found'
                raise Exception('DMM-未匹配到番号')                    
            result, htmlcode = get_html(url, cookies=cookies)   # 获取详情页内容
            html = etree.fromstring(htmlcode, etree.HTMLParser())
        actor = getActor(html)  # 获取歌手
        title = getTitle(html).strip(actor) # 获取标题（去掉标题最后的歌手名）
        if not title:
            log_info += '   >>> DMM- title 获取失败！ \n'
            error_type = 'need login'
            raise Exception('DMM- title 获取失败！')
        cover_url = getCover(html) # 获取cover
        if not cover_url:
            log_info += '   >>> DMM- cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('DMM- cover url 获取失败！')
        try:
            studio = str(getStudio(html))
            outline = getOutline(html)
            score = getScore(html)
            runtime = getRuntime(html)
            director = getDirector(html)
            release = getRelease(html)
            # number = getNum(html)
            tag = getTag(html)
            series = getSeries(html).replace('-', '')
            year = getYear(release)
            extrafanart = getExtraFanart(html)
            actor_photo = getActorPhoto(actor)
        except Exception as error_info:
                log_info += '   >>> DMM-获取data信息时出错(dmm.py)！ 错误信息：%s\n' % str(error_info)
                error_info = str(error_info)
                raise Exception(log_info)            
        try:
            dic = {
                'title': title,
                'number': number,
                'actor': actor,
                'outline': outline,
                'tag': tag,
                'release': release,
                'year': year,
                'runtime': runtime,
                'score': score,
                'series': series,
                'director': director,
                'studio': studio,
                'publisher': studio,
                'source': 'dmm.main',
                'website': url,
                'actor_photo': actor_photo,
                'cover': str(cover_url),
                'cover_small': '',
                'extrafanart': extrafanart,
                'imagecut': 1,
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
            }
            log_info += '   >>> DMM-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
                log_info += '   >>> DMM-生成数据字典：出错！ 错误信息：%s\n' % str(error_info)
                error_info = str(error_info)
                raise Exception(log_info)

    except Exception as error_info:
        dic = {
            'title': '',
            'cover': '',
            'website': str(url).strip('[]'),
            'log_info': str(log_info),
            'error_type': str(error_type),
            'error_info': str(error_info),
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))  # .encode('UTF-8')
    return js


# print(main('snis-027'))
# print(main('ipx-292'))
# print(main('wicp-002'))
# print(main('ssis-080'))
# print(main('ssis-080'))
# main('DV-1562')
# print(main('mide00139', "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=mide00139"))
# print(main('mide00139', ""))
# print(main('kawd00969'))
