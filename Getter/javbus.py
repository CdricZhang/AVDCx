import re
from lxml import etree
import json
from Function.getHtml import get_html, post_html
from configparser import RawConfigParser
import urllib3
urllib3.disable_warnings()

def getDelActorName():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    del_actor_name = config.getint('Name_Rule', 'del_actor_name')
    return del_actor_name

def getTitle(html):
    result = html.xpath('//h3/text()')
    if result:
        result = result[0].replace('&', '')
    else:
        result = ''
    return result

def getWebNumber(html):
    result = html.xpath('//span[@class="header"][contains(text(), "識別碼:")]/../span[2]/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getActor(html):
    try:
        result = str(html.xpath('//div[@class="star-name"]/a/text()')).strip(" ['']").replace("'", '').replace(', ', ',')
    except:
        result = ''
    return result

def getActorPhoto(html, url):
    actor = html.xpath('//div[@class="star-name"]/../a/img/@title')
    photo = html.xpath('//div[@class="star-name"]/../a/img/@src')
    data = {}
    if len(actor) == len(photo):
        for i in range(len(actor)):
            data[actor[i]] = url + photo[i]
    else:
        for each in actor:
            data[each] = ''
    return data

def getCover(html, url):  # 获取封面链接
    result = html.xpath('//a[@class="bigImage"]/@href')
    if result:
        cover_url = url + result[0]
    else:
        cover_url = ''
    return cover_url

def getRelease(html):  # 获取发行日期
    result = html.xpath('//span[@class="header"][contains(text(), "發行日期:")]/../text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result

def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release[:4]

def getMosaic(html):
    select_tab = html.xpath('//li[@class="active"]/a/text()')
    if select_tab == '有碼':
        mosaic = '有码'
    else:
        mosaic = '无码'
    return mosaic

def getRuntime(html):
    result = html.xpath('//span[@class="header"][contains(text(), "長度:")]/../text()')
    if result:
        result = result[0].strip()
        result = re.findall('\d+', result)
        if result:
            result = result[0]
        else:
            result = ''
    else:
        result = ''
    return result

def getStudio(html):
    result = html.xpath('//a[contains(@href, "/studio/")]/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result

def getPublisher(html, studio):  # 获取发行商
    result = html.xpath('//a[contains(@href, "/label/")]/text()')
    if result:
        result = result[0].strip()
    else:
        result = studio
    return result

def getDirector(html):  # 获取导演
    result = html.xpath('//a[contains(@href, "/director/")]/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result

def getSeries(html):
    result = html.xpath('//a[contains(@href, "/series/")]/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result


def getExtraFanart(html, url):  # 获取封面链接
    result = html.xpath("//div[@id='sample-waterfall']/a/@href")
    if result:
        new_list = []
        for each in result:
            each = url + each
            new_list.append(each)
    else:
        new_list = ''
    return new_list


def getTag(html):  # 获取标签
    result = html.xpath('//span[@class="genre"]/label/a[contains(@href, "/genre/")]/text()')
    if result:
        result = str(result).strip(" ['']").replace("'", "").replace(', ', ',')
    else:
        result = ''
    return result


def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> javbus '
    log_info += '   >>> javbus-开始使用 javbus 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    error_type = ''
    error_info = ''
    dic = {}
    try:
        if not real_url:
            real_url = 'https://www.javbus.com/' + number.upper()
        result, htmlcode = get_html(real_url)
        if not result:
            log_info += '   >>> javbus-请求详情页：错误！信息：' + htmlcode
            error_type = 'timeout'
            raise Exception('javbus请求详情页：错误！信息：' + htmlcode)
        if '404 Page Not Found!' in htmlcode:
            log_info += '   >>> javbus-未匹配到番号！'
            error_type = 'not found'
            raise Exception('javbus-未匹配到番号！')           
        html_info = etree.fromstring(htmlcode, etree.HTMLParser())
        title = getTitle(html_info)
        if not title:
            log_info += '   >>> javbus-title 获取失败！ \n'
            error_type = 'javbus-title 获取失败！'
            raise Exception('javbus-title 获取失败!')
        web_number = getWebNumber(html_info)    # 获取番号，用来替换标题里的番号
        title = title.strip(web_number).strip()
        actor = getActor(html_info) # 获取actor
        actor_photo = getActorPhoto(html_info, 'https://www.javbus.com')
        if getDelActorName():
            title = title.strip(' ' + actor)
        cover_url = getCover(html_info, 'https://www.javbus.com') # 获取cover
        if 'http' not in cover_url:
            log_info += '   >>> javbus-cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('javbus-cover url 获取失败!')
        release = getRelease(html_info)
        year = getYear(release)
        tag = getTag(html_info)
        mosaic = getMosaic(html_info)
        if mosaic == '无码':
            imagecut = 3
        runtime = getRuntime(html_info)
        studio = getStudio(html_info)
        publisher = getPublisher(html_info, studio)
        director = getDirector(html_info)
        series = getSeries(html_info)
        extrafanart = getExtraFanart(html_info, 'https://www.javbus.com/')
        try:
            dic = {
                'title': title,
                'number': number,
                'actor': actor,
                'outline': '',
                'tag': tag,
                'release': release,
                'year': year,
                'runtime': runtime,
                'score': '',
                'series': series,
                'director': director,
                'publisher': publisher,
                'studio': studio,
                'source': 'javbus',
                'website': real_url,
                'search_url': '',
                'actor_photo': actor_photo,
                'cover': cover_url,
                'cover_small': '',
                'extrafanart': extrafanart,
                'imagecut': imagecut,
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
                'req_web': req_web,
                'mosaic': mosaic,
            }
            log_info += '   >>> javbus-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
            log_info += '   >>> javbus-生成数据字典：出错！ 错误信息：%s \n' % str(error_info)
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

def main_us(number, appoint_url='', log_info='', req_web=''):
    number = number.replace('-', '.')
    req_web += '-> javbus[us] '
    log_info += '   >>> javbus-开始使用 javbus[us] 进行刮削\n'
    real_url = appoint_url
    url_search = ''
    title = ''
    cover_url = ''
    error_type = ''
    error_info = ''
    dic = {}
    try:
        if not real_url:
            # 通过搜索获取real_url
            url_search = 'https://www.javbus.red/search/' + number
            log_info += '   >>> javbus-生成搜索页地址: %s\n' % url_search
            # ========================================================================搜索番号
            result, html_search = get_html(url_search)
            if not result:
                log_info += '   >>> javbus-请求搜索页：错误！信息：' + html_search
                error_type = 'timeout'
                raise Exception('javbus-请求搜索页：错误！信息：' + html_search)
            html = etree.fromstring(html_search, etree.HTMLParser())
            real_url = html.xpath("//div[@class='photo-info']/span/date[contains(text(), $number)]/../../../@href", number=number)

            if real_url:
                real_url = real_url[0]
                log_info += '   >>> javbus-匹配详情页地址： %s \n' % real_url
            else:
                log_info += '   >>> javbus-搜索结果页匹配番号：未匹配到番号！ \n'
                error_type = 'javbus-搜索结果页匹配番号：未匹配到番号！'
                raise Exception('javbus-搜索结果页匹配番号：未匹配到番号！')
        if real_url:
            try:
                result, html_content = get_html(real_url)
            except Exception as error_info:
                log_info += '   >>> javbus-请求详情页：出错！错误信息：%s \n' % str(error_info)
                error_type = 'timeout'
                raise Exception('javbus-请求详情页：出错！错误信息：%s \n' % str(error_info))          
            html_info = etree.fromstring(html_content, etree.HTMLParser())

            title = getTitle(html_info)
            if not title:
                log_info += '   >>> javbus-title 获取失败！ \n'
                error_type = 'javbus-title 获取失败！'
                raise Exception('javbus-title 获取失败!')
            web_number = getWebNumber(html_info)    # 获取番号，用来替换标题里的番号
            title = title.strip(web_number).strip()
            actor = getActor(html_info) # 获取actor
            actor_photo = getActorPhoto(html_info, '')
            if getDelActorName():
                title = title.strip(' ' + actor)
            cover_url = getCover(html_info, '') # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> javbus-cover url 获取失败！ \n'
                error_type = 'Cover Url is None!'
                raise Exception('javbus-cover url 获取失败!')
            release = getRelease(html_info)
            year = getYear(release)
            tag = getTag(html_info)
            mosaic = getMosaic(html_info)
            if mosaic == '无码':
                imagecut = 3
            runtime = getRuntime(html_info)
            studio = getStudio(html_info)
            publisher = getPublisher(html_info, studio)
            director = getDirector(html_info)
            series = getSeries(html_info)
            extrafanart = getExtraFanart(html_info, '')
            try:
                dic = {
                    'title': title,
                    'number': number,
                    'actor': actor,
                    'outline': '',
                    'tag': tag,
                    'release': release,
                    'year': year,
                    'runtime': runtime,
                    'score': '',
                    'series': series,
                    'director': director,
                    'publisher': publisher,
                    'studio': studio,
                    'source': 'javbus',
                    'website': real_url,
                    'search_url': url_search,
                    'actor_photo': actor_photo,
                    'cover': cover_url,
                    'cover_small': '',
                    'extrafanart': extrafanart,
                    'imagecut': imagecut,
                    'log_info': str(log_info),
                    'error_type': '',
                    'error_info': str(error_info),
                    'req_web': req_web,
                    'mosaic': mosaic,
                }
                log_info += '   >>> javbus-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> javbus-生成数据字典：出错！ 错误信息：%s \n' % str(error_info)
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


# print(main('070621_001'))
# print(main('ssni-644'))
# print(main_us('BigTitsatWork-17-09-26'))
# print(main_us('BrazzersExxtra.21.02.01'))
# print(main('KA-001'))
# print(main('010115-001'))
# print(main('012715-793'))
# print(main('heyzo-1031'))

# print(main('ssni-644', "https://www.javbus.com/SSNI-644"))
# print(main('ssni-802', ""))
# print(main_us('DirtyMasseur.20.07.26', "https://www.javbus.one/DirtyMasseur-20-07-26"))
