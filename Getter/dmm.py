#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys  # NOQA: E402
sys.path.append('../')  # NOQA: E402
import re
from lxml import etree
import json
from Function.getHtml import get_html
import urllib3
urllib3.disable_warnings()


def getTitle(html):
    result1 = html.xpath('//h1[@id="title"]/text()')
    result2 = html.xpath('//h1[@class="item fn bold"]/text()')
    a = ''
    b = ''
    if result1:
        a = result1[0].strip('"')
    if result2:
        b = result2[0].strip('"')
    return a + b


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
    result = html.xpath(
        "//td[contains(text(),'収録時間')]/following-sibling::td/text()")
    if result:
        return re.search('\d+', str(result[0])).group()
    return ''


def getSeries(html):
    result = html.xpath(
        "//td[contains(text(),'シリーズ：')]/following-sibling::td/a/text()")
    if result:
        return result[0]
    return ''


def getNum(html):
    result = html.xpath(
        "//td[contains(text(),'品番：')]/following-sibling::td/text()")
    if result:
        return result[0]
    return ''


def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release[:4]


def getRelease(html):
    result = html.xpath(
        "//td[contains(text(),'発売日：')]/following-sibling::td/text()")
    if result:
        return result[0].lstrip('\n')
    return ''


def getTag(html):
    result = str(html.xpath(
        "//td[contains(text(),'ジャンル：')]/following-sibling::td/a/text()"))
    if result:
        return str(result).strip(" ['']").replace("', '", ",")
    return ''


def getCover(html):
    result = html.xpath('//a[@name="package-image"]/@href')
    if result:
        return result[0]
    return ''


def getCoverSmall(html):
    result = html.xpath('//img[@class="tdmm"]/@src')
    if result:
        return result[0]
    return ''


def getExtraFanart(html):
    result = html.xpath("//div[@id='sample-image-block']/a/img/@src")
    if result:
        return result
    return ''


def getDirector(html):
    result = html.xpath(
        "//td[contains(text(),'監督：')]/following-sibling::td/a/text()")
    if result:
        return result[0]
    return ''


def getOutline(html):
    result1 = html.xpath("//div[@class='mg-b20 lh4']/text()")
    result2 = html.xpath(
        "//div[@class='mg-b20 lh4']/p[@class='mg-b20']/text()")
    a = ''
    b = ''
    if result1:
        a = result1[0].replace('\\n', '').replace('\n', '').strip()
    if result2:
        b = result2[0].replace('\\n', '').replace('\n', '').strip()
    return a + b


def getScore(html):
    result = html.xpath("//p[@class='d-review__average']/strong/text()")
    if result:
        return result[0].replace('\\n', '').replace('\n', '').replace('点', '')
    return ''


def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> dmm '
    cookies = {'cookie': 'uid=abcd786561031111; age_check_done=1;'}
    log_info += '   >>> [ DMM ] 开始使用 dmm 进行刮削\n'
    title = ''
    cover_url = ''
    cover_small_url = ''
    image_download = False
    image_cut = 'right'
    error_type = ''
    error_info = ''
    dic = {}
    new_number = number.lower().replace('-', '')
    url = 'https://www.dmm.co.jp/search/=/searchstr=' + new_number
    num1 = '/cid=' + new_number + '/'
    num2 = new_number + '/'

    if appoint_url:  # 如果传入地址，则使用传入的地址
        url = appoint_url
    try:
        result, htmlcode = get_html(url, cookies=cookies)
        # 对各种错误、限制进行判断
        if not result:  # 请求失败
            error_type = 'request error'  # error_type 只是标记失败，内容暂不展示，可随便写
            error_info = '[ DMM ] 请求URL：%s 出现错误：%s' % (
                url, htmlcode)   # error_info 在主界面标题位置展示
            # log_info 在日志页面展示
            log_info += '   >>> [ DMM ] 请求URL：%s 出现错误：%s\n' % (url, htmlcode)
            raise
        if re.findall('foreignError', htmlcode):    # 非日本地区限制访问
            error_type = 'area error'
            error_info = '[ DMM ] 地域限制, 请使用日本节点访问！'
            log_info += '   >>> [ DMM ] 地域限制, 请使用日本节点访问！\n'
            raise
        html = etree.fromstring(htmlcode, etree.HTMLParser())

        # 解析搜索页，如果是传入url，则跳过此环节
        if not appoint_url:
            # 匹配详情页地址
            url = ''
            # 优先匹配'/cid=snis126/'这样链接的，图上面没有蓝光水印
            url1 = html.xpath("//a[contains(@href, $val)]/@href", val=num1)
            # /cid=6snis027/ 如果链接中包含detail和number，则表示找到了
            url2 = html.xpath(
                "//a[contains(@href, 'detail')][contains(@href, $val)]/@href", val=num2)

            if url1:
                url = url1[0]
            elif url2:
                if re.search('cid=\d+[a-zA-Z]+\d+', url2[0]):
                    url = url2[0]
            if not url:
                error_type = 'not found the movie'
                error_info = '[ DMM ] 搜索页未匹配到番号！'
                log_info += '   >>> [ DMM ] 搜索页未匹配到番号！\n'
                raise
            if url.find('?i3_ref=search&i3_ord') != -1:  # 去除url中无用的后缀
                url = url[:url.find('?i3_ref=search&i3_ord')]
            result, htmlcode = get_html(url, cookies=cookies)
            html = etree.fromstring(htmlcode, etree.HTMLParser())

        # 分析详情页
        if re.findall('ageCheck', htmlcode):   # 年龄认证，表示无cookie或cookie失效
            if cookies['cookie']:
                error_info = '[ DMM ] 年龄认证！需要重新设置cookie！'
                log_info += '   >>> [ DMM ] 年龄认证！需要重新设置cookie！\n'
            else:
                error_info = '[ DMM ] 年龄认证！请到【设置】-【网络设置】中添加 cookie！'
                log_info += '   >>> [ DMM ] 年龄认证！请到【设置】-【网络设置】中添加 cookie！\n'
            raise
        # 如果页面有404，表示传入的页面地址不对
        if '404 Not Found' in str(html.xpath("//span[@class='d-txten']/text()")):
            error_type = 'detail page url error 404 not found!'
            error_info = '[ DMM ] 详情页地址不对！404 Not Found!'
            log_info += '   >>> [ DMM ] 详情页地址不对！404 Not Found！\n'
            raise

        actor = getActor(html)  # 获取歌手
        title = getTitle(html).strip()  # 获取标题（去掉标题最后的歌手名）
        if not title:
            error_type = 'title data not found'
            error_info = '[ DMM ]  标题数据未匹配到！'
            log_info += '   >>> [ DMM ]  标题数据未匹配到！ \n'
            raise
        cover_url = getCover(html)  # 获取cover
        if not cover_url:
            error_type = 'cover URL not found'
            error_info += '[ DMM ]  cover URL 未匹配到！'
            log_info += '   >>> [ DMM ]  cover URL 未匹配到！ \n'
            raise
        try:
            outline = getOutline(html)
            tag = getTag(html)
            release = getRelease(html)
            year = getYear(release)
            runtime = getRuntime(html)
            score = getScore(html)
            series = getSeries(html)
            director = getDirector(html)
            # number = getNum(html)
            studio = getStudio(html)
            extrafanart = getExtraFanart(html)
            cover_small_url = getCoverSmall(html)
            actor_photo = getActorPhoto(actor)
        except Exception as error_info:
            error_type = 'error'
            error_info = '[ DMM ] 一些 data 在获取时出错！'
            log_info += '   >>> [ DMM ] 一些 data 在获取时出错！！ %s\n' % str(
                error_info)
            raise
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
                'source': 'dmm',
                'website': url,
                'actor_photo': actor_photo,
                'cover': str(cover_url),
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
            log_info += '   >>> [ DMM ] 数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
            error_type = 'dic error'
            error_info = '[ DMM ] 生成数据字典时出错！'
            log_info += '   >>> [ DMM ] 生成数据字典时出错！ %s\n' % str(error_info)
            raise

    except:
        dic = {
            'title': '',
            'cover': '',
            'website': str(url),
            'log_info': str(log_info),
            'error_type': str(error_type),
            'error_info': str(error_info),
            'req_web': req_web,
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False,
                    indent=4, separators=(',', ':'))  # .encode('UTF-8')
    return js


if __name__ == '__main__':
    print(main('ssni888'))
    # print(main('snis-027'))
    # print(main('n1581'))
    # print(main('ssni-888'))
    # print(main('ssni00888'))
    # print(main('ssni00999'))
    # print(main('ipx-292'))
    # print(main('wicp-002'))
    # print(main('ssis-080'))
    # print(main('DV-1562'))
    # print(main('mide00139', "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=mide00139"))
    # print(main('mide00139', ""))
    # print(main('kawd00969'))
