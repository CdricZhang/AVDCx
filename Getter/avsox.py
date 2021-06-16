import json
import re
from bs4 import BeautifulSoup
from lxml import etree
from Function.getHtml import get_html


def getActorPhoto(htmlcode):  # //*[@id="star_qdt"]/li/a/img
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'avatar-box'})
    d = {}
    for i in a:
        l = i.img['src']
        t = i.span.get_text()
        p2 = {t: l}
        d.update(p2)
    return d


def getTitle(a):
    try:
        html = etree.fromstring(a, etree.HTMLParser())
        result = str(html.xpath('/html/body/div[2]/h3/text()')).strip(" ['']")  # [0]
        return result.replace('/', '')
    except:
        return ''


def getActor(a):  # //*[@id="center_column"]/div[2]/div[1]/div/table/tbody/tr[1]/td/text()
    soup = BeautifulSoup(a, 'lxml')
    a = soup.find_all(attrs={'class': 'avatar-box'})
    d = []
    for i in a:
        d.append(i.span.get_text())
    return d


def getStudio(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//p[contains(text(),"制作商: ")]/following-sibling::p[1]/a/text()')).strip(" ['']").replace(
        "', '", ' ')
    return result1


def getRuntime(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//span[contains(text(),"长度:")]/../text()')).strip(" ['分钟']")
    return result1


def getSeries(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//p[contains(text(),"系列:")]/following-sibling::p[1]/a/text()')).strip(" ['']")
    return result1


def getNum(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//span[contains(text(),"识别码:")]/../span[2]/text()')).strip(" ['']")
    return result1


def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release


def getRelease(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//span[contains(text(),"发行时间:")]/../text()')).strip(" ['']")
    return result1


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div[1]/div[1]/a/img/@src')).strip(" ['']")
    return result


def getCover_small(htmlcode, count):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    cover_small = html.xpath("//div[@id='waterfall']/div[" + str(count) + "]/a/div[@class='photo-frame']/img/@src")[0]
    return cover_small


def getTag(a):  # 获取演员
    soup = BeautifulSoup(a, 'lxml')
    a = soup.find_all(attrs={'class': 'genre'})
    d = []
    for i in a:
        d.append(i.get_text())
    return d


def getUrl(number):
    result, response = get_html('https://avsox.website/cn/search/' + number)
    html = etree.fromstring(response, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    url_list = html.xpath('//*[@id="waterfall"]/div/a/@href')

    if len(url_list) > 0:
        for i in range(1, len(url_list) + 1):
            number_get = str(html.xpath(
                '//*[@id="waterfall"]/div[' + str(i) + ']/a/div[@class="photo-info"]/span/date[1]/text()')).strip(
                " ['']")
            if number.upper() == number_get.upper():
                page_url = 'https:' + url_list[i-1]
                return i, response, page_url, result
                # return i, response, str(html.xpath('//*[@id="waterfall"]/div[' + str(i) + ']/a/@href')).strip(" ['']")
    return 0, response, '', result


def main(number, appoint_url='', log_info=''):
    log_info += '   >>> AVSOX-开始使用 avsox 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    dic = {}
    try:
        count, response, url, result = getUrl(number)
        if str(result) == 'error':
            log_info += '   >>> AVSOX-请求详情页：超时！请检测网络或代理！'
            error_type = 'timeout'
            raise Exception('>>> AVSOX-请求详情页：出错！请检测网络或代理！')
        if appoint_url != '':
            url = appoint_url
        elif url == '':
            log_info += '   >>> AVSOX-未匹配到番号！ \n'
            error_type = 'Movie not found'
            raise Exception('Movie not found')

        result, web = get_html(url)
        soup = BeautifulSoup(web, 'lxml')
        info = str(soup.find(attrs={'class': 'row movie'}))
        number = getNum(web)
        title = getTitle(web).strip(number).strip().replace(' ', '-'), # 获取标题
        if not title:
            log_info += '   >>> AVSOX- title 获取失败！ \n'
            error_type = 'need login'
            raise Exception('>>> AVSOX- title 获取失败！')
        cover_url = getCover(web) # 获取cover
        if 'http' not in cover_url:
            log_info += '   >>> AVSOX- cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('>>> AVSOX- cover url 获取失败！')
        cover_small = getCover_small(response, count)
        if 'http' not in cover_small:
            log_info += '   >>> AVSOX- cover url 获取失败！\n'
            error_type = 'Cover_small Url is None!'
            raise Exception('>>> AVSOX- cover_small url 获取失败！')
        try:
            dic = {
                'actor': getActor(web),
                'title': str(title),
                'studio': getStudio(info),
                'runtime': getRuntime(info),
                'release': getRelease(info),
                'number': getNum(info),
                'tag': getTag(web),
                'series': getSeries(info),
                'year': getYear(getRelease(info)),
                'actor_photo': getActorPhoto(web),
                'cover': str(cover_url),
                'cover_small': str(cover_small),
                'extrafanart': '',
                'imagecut': 3,
                'director': '',
                'publisher': '',
                'outline': '',
                'score': '',
                'website': url,
                'source': 'avsox.website',
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
            }
            log_info += '   >>> AVSOX-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
                log_info += '   >>> AVSOX-生成数据字典：出错！ 错误信息：%s\n' % error_info
                error_info = error_info
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
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


# print(main('051119-917'))
# print(main('032620_001'))
# print(main('032620_001', 'https://avsox.website/cn/movie/cb8d28437cff4e90'))