import re
from lxml import etree
import json
from Function.getHtml import post_html


def getActorPhoto(actor):
    actor = actor.split(',')
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


def getStudio(html):
    result = str(html.xpath('//div[@class="col-md-9"]/a[contains(@href,"/company/")]/text()')).strip(" ['']")
    return result

def getRuntime(response):
    return str(re.findall(r'<b>収録時間</b>: (\d+) \S+<br>', response)).strip(" ['']")


def getSeries(html):
    result = str(html.xpath('//div[@class="col-md-9"]/a[contains(@href,"/series/")]/text()')).strip(" ['']")
    return result


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


def main(number, appoint_url='', log_info='', req_web='', isuncensored=False):
    req_web += '-> jav321'
    log_info += '   >>> JAV321-开始使用 jav321 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small_url = ''
    image_download = False
    image_cut = 'right'
    error_type = ''
    error_info = ''
    try:
        result_url = "https://www.jav321.com/search"
        if appoint_url != '':
            result_url = appoint_url
        result, response = post_html(result_url, query={"sn": number})
        if not result:
            log_info += '   >>> JAV321-请求搜索页：错误！信息：' + response
            error_type = 'timeout'
            raise Exception('>>> JAV321-请求搜索页：错误！信息' + response)
        if 'AVが見つかりませんでした' in response:
            log_info += '   >>> JAV321-未匹配到番号！ \n'
            error_type = 'Movie data not found'
            raise Exception('JAV321-未匹配到番号')
        detail_page = etree.fromstring(response, etree.HTMLParser())
        actor = getActor(response)
        actor_photo = getActorPhoto(actor)
        title = getTitle(response).strip() # 获取标题
        if not title:
            log_info += '   >>> JAV321- title 获取失败！ \n'
            error_type = 'need login'
            raise Exception('>>> JAV321- title 获取失败！]')
        cover_url = getCover(detail_page) # 获取cover
        cover_small_url = getCoverSmall(detail_page)
        if not cover_url:
            cover_url = cover_small_url
        if 'http' not in cover_url:
            log_info += '   >>> JAV321- cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('>>> JAV321- cover url 获取失败！]')
        release = getRelease(response)
        year = getYear(release)
        runtime = getRuntime(response)
        if isuncensored:
            image_cut = 'center'
        number = getNum(response)
        outline = getOutline(detail_page)
        tag = getTag(response)
        score = getScore(response)

        studio = getStudio(detail_page)
        series = getSeries(detail_page)
        extrafanart = getExtraFanart(detail_page)
        website = getWebsite(detail_page)
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
                'director': '',
                'studio': studio,
                'publisher': studio,
                'source': 'jav321',
                'website': website,
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
            'req_web': req_web,
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


# print(main('blk-495'))
# print(main('snis-333'))
# print(main('GERK-326'))
# print(main('msfh-010'))

# print(main('msfh-010'))
# print(main('kavr-065'))
# print(main('ssni-645'))
# print(main('sivr-038'))
# print(main('ara-415'))
# print(main('luxu-1257'))
# print(main('heyzo-1031'))
# print(main('ABP-905'))
# print(main('heyzo-1031', ''))
# print(main('ymdd-173', 'https://www.jav321.com/video/ymdd00173'))
