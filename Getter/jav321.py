import re
from lxml import etree
import json
from Function.getHtml import post_html


def getActorPhoto(actor):
    data = {}
    for i in actor:
        actor_photo = {i: ''}
        data.update(actor_photo)
    return data


def getTitle(response):
    return str(re.findall(r'<h3>(.+) <small>', response)).strip(" ['']")


def getActor(response):
    if re.search(r'<a href="/star/\S+">(\S+)</a> &nbsp;', response):
        return str(re.findall(r'<a href="/star/\S+">(\S+)</a> &nbsp;', response)).strip(" [',']").replace('\'', '')
    elif re.search(r'<a href="/heyzo_star/\S+">(\S+)</a> &nbsp;', response):
        return str(re.findall(r'<a href="/heyzo_star/\S+">(\S+)</a> &nbsp;', response)).strip(" [',']").replace('\'',
                                                                                                                '')
    else:
        return str(re.findall(r'<b>出演者</b>: ([^<]+) &nbsp; <br>', response)).strip(" [',']").replace('\'', '')


def getStudio(response):
    return str(re.findall(r'<a href="/company/\S+">(\S+)</a>', response)).strip(" ['']")


def getRuntime(response):
    return str(re.findall(r'<b>収録時間</b>: (\d+) \S+<br>', response)).strip(" ['']")


def getSeries(response):
    return str(re.findall(r'<b>系列</b>: <a href="/series/\S+">(\S+)</a>', response)).strip(" ['']")


def getWebsite(detail_page):
    return 'https:' + detail_page.xpath('//a[contains(text(),"简体中文")]/@href')[0]


def getNum(response):
    return str(re.findall(r'<b>品番</b>: (\S+)<br>', response)).strip(" ['']").upper()


def getScore(response):
    if re.search(r'<b>平均評価</b>: <img data-original="/img/(\d+).gif" />', response):
        score = re.findall(r'<b>平均評価</b>: <img data-original="/img/(\d+).gif" />', response)[0]
        return str(float(score) / 10.0)
    else:
        return str(re.findall(r'<b>平均評価</b>: ([^<]+)<br>', response)).strip(" [',']").replace('\'', '')


def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release


def getRelease(response):
    return str(re.findall(r'<b>配信開始日</b>: (\d+-\d+-\d+)<br>', response)).strip(" ['']").replace('0000-00-00', '')


def getCover(detail_page):
    cover_url = str(detail_page.xpath("/html/body/div[@class='row'][2]/div[@class='col-md-3']/div[@class='col-xs-12 "
                                      "col-md-12'][1]/p/a/img[@class='img-responsive']/@src")).strip(" ['']")
    if cover_url == '':
        cover_url = str(
            detail_page.xpath("//*[@id='vjs_sample_player']/@poster")).strip(" ['']")
    return cover_url


def getExtraFanart(htmlcode):
    extrafanart_list = htmlcode.xpath("/html/body/div[@class='row'][2]/div[@class='col-md-3']/div[@class='col-xs-12 col-md-12']/p/a/img[@class='img-responsive']/@src")
    return extrafanart_list


def getCoverSmall(detail_page):
    return str(detail_page.xpath('//img[@class="img-responsive"]/@src')[0])


def getTag(response):  # 获取演员
    return re.findall(r'<a href="/genre/\S+">(\S+)</a>', response)


def getOutline(detail_page):
    return str(detail_page.xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/div/text()')).strip(" ['']")


def main(number, appoint_url='', log_info='', isuncensored=False):
    log_info += '   >>> JAV321-开始使用 jav321 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    try:
        result_url = "https://www.jav321.com/search"
        if appoint_url != '':
            result_url = appoint_url
        result, response = post_html(result_url, query={"sn": number})
        if result == 'error':
            log_info += '   >>> JAV321-请求搜索页：错误！信息：' + response
            error_type = 'timeout'
            raise Exception('>>> JAV321-请求搜索页：错误！信息' + response)
        if 'AVが見つかりませんでした' in response:
            log_info += '   >>> JAV321-未匹配到番号！ \n'
            error_type = 'Movie not found'
            raise Exception('JAV321-未匹配到番号')
        detail_page = etree.fromstring(response, etree.HTMLParser())
        title = getTitle(response) # 获取标题
        if not title:
            log_info += '   >>> JAV321- title 获取失败！ \n'
            error_type = 'need login'
            raise Exception('>>> JAV321- title 获取失败！]')
        cover_url = getCover(detail_page) # 获取cover
        cover_small = getCoverSmall(detail_page)
        if not cover_url:
            cover_url = cover_small
        if 'http' not in cover_url:
            log_info += '   >>> JAV321- cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('>>> JAV321- cover url 获取失败！]')
        release = getRelease(response)
        actor = getActor(response)
        imagecut = 1
        if 'HEYZO' in number.upper() or isuncensored:
            imagecut = 3
            if cover_small == '':
                imagecut = 0
        studio = getStudio(response)
        try:
            dic = {
                'title': str(title),
                'number': getNum(response),
                'actor': actor,
                'outline': getOutline(detail_page),
                'tag': getTag(response),
                'release': str(release),
                'year': getYear(release),
                'runtime': getRuntime(response),
                'score': getScore(response),
                'series': getSeries(response),
                'director': '',
                'studio': studio,
                'publisher': studio,
                'source': 'jav321.main',
                'website': getWebsite(detail_page),
                'actor_photo': getActorPhoto(actor.split(',')),
                'cover': str(cover_url),
                'cover_small': str(cover_small),
                'extrafanart': getExtraFanart(detail_page),
                'imagecut': imagecut,
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
            }
            log_info += '   >>> JAV321-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
            log_info += '   >>> JAV321-生成数据字典：出错！ 错误信息：%s\n' % str(error_info)
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


# print(main('GERK-326'))
# print(main('msfh-010'))

'''
print(main('msfh-010'))
print(main('kavr-065'))
print(main('ssni-645'))
print(main('sivr-038'))
print(main('ara-415'))
print(main('luxu-1257'))
print(main('heyzo-1031'))
print(main('ABP-905'))
'''
# print(main('heyzo-1031', ''))
# print(main('ymdd-173', 'https://www.jav321.com/video/ymdd00173'))
