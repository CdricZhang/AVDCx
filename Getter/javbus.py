import re
from lxml import etree
import json
from Function.getHtml import get_html
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
        result = result[0]
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
            if 'http' not in photo[i]:
                data[actor[i]] = url + photo[i]
            else:
                data[actor[i]] = photo[i]
    else:
        for each in actor:
            data[each] = ''
    return data

def getCover(html, url):  # 获取封面链接
    result = html.xpath('//a[@class="bigImage"]/@href')
    if result:
        if 'http' not in result[0]:
            cover_url = url + result[0]
        else:
            cover_url = result[0]
    else:
        cover_url = ''
    return cover_url

def getCoverSmall(cover_url):  # 获取小封面链接
    cover_small_url = ''
    if '/pics/' in cover_url:
        cover_small_url = cover_url.replace('/cover/', '/thumb/').replace('_b.jpg', '.jpg')
    elif '/imgs/' in cover_url:
        cover_small_url = cover_url.replace('/cover/', '/thumbs/').replace('_b.jpg', '.jpg')
    return cover_small_url

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
    select_tab = str(html.xpath('//li[@class="active"]/a/text()'))
    if '有碼' in select_tab:
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
            if 'http' not in each:
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

def getRealUrl(number, url_type):  # 获取详情页链接
    if url_type == 'us':
        url_search = 'https://www.javbus.red/search/' + number
    elif url_type == 'censored':
        url_search = 'https://www.javbus.com/search/' + number + '&type=&parent=ce'
    else:
        url_search = 'https://www.javbus.com/uncensored/search/' + number + '&type=0&parent=uc'
    # ========================================================================搜索番号
    result, html_search = get_html(url_search)
    if not result:
        return False
    html = etree.fromstring(html_search, etree.HTMLParser())
    url_list = html.xpath("//a[@class='movie-box']/@href")
    for each in url_list:
        if number.upper().replace('.', '').replace('-', '') in each.upper().replace('-', ''):
            return each
    return False

def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> javbus '
    log_info += '   >>> javbus-开始使用 javbus 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small_url = ''
    error_type = ''
    error_info = ''
    image_download = False
    image_cut = 'right'
    dic = {}
    try:
        if not real_url:
            real_url = 'https://www.javbus.com/' + number
            if re.search('[-_]\d{2}[-_]\d{2}[-_]\d{2}', number):    # 欧美影片
                number = number.replace('-', '.').replace('_', '.')
            if '.' in number:
                real_url = getRealUrl(number, 'us')
                if not real_url:
                    log_info += '   >>> javbus-未匹配到番号！'
                    error_type = 'not found'
                    raise Exception('javbus-未匹配到番号！')                    
        result, htmlcode = get_html(real_url)
        if not result:
            log_info += '   >>> javbus-请求详情页：错误！信息：' + htmlcode
            error_type = 'timeout'
            raise Exception('javbus请求详情页：错误！信息：' + htmlcode)
        if '404 Page Not Found!' in htmlcode:
            real_url = getRealUrl(number, 'censored')
            if real_url:
                result, htmlcode = get_html(real_url)
            else:
                real_url = getRealUrl(number, 'uncensored')
                if real_url:
                    result, htmlcode = get_html(real_url)
                else:
                    log_info += '   >>> javbus-未匹配到番号！'
                    error_type = 'not found'
                    raise Exception('javbus-未匹配到番号！')           
        html_info = etree.fromstring(htmlcode, etree.HTMLParser())
        title = getTitle(html_info)
        if not title:
            log_info += '   >>> javbus-title 获取失败！ \n'
            error_type = 'javbus-title 获取失败！'
            raise Exception('javbus-title 获取失败!')
        number = getWebNumber(html_info)    # 获取番号，用来替换标题里的番号
        title = title.replace(number, '').strip()
        actor = getActor(html_info) # 获取actor
        actor_photo = getActorPhoto(html_info, 'https://www.javbus.com')
        if getDelActorName():
            title = title.replace(' ' + actor, '')
        cover_url = getCover(html_info, 'https://www.javbus.com') # 获取cover
        cover_small_url = getCoverSmall(cover_url)
        if 'http' not in cover_url:
            log_info += '   >>> javbus-cover url 获取失败！ \n'
            error_type = 'Cover Url is None!'
            raise Exception('javbus-cover url 获取失败!')
        release = getRelease(html_info)
        year = getYear(release)
        tag = getTag(html_info)
        mosaic = getMosaic(html_info)
        if mosaic == '无码':
            image_cut = 'center'
            if '_' in number and cover_small_url:   # 一本道，并且有小图时，下载poster
                image_download = True
            elif 'HEYZO' in number and len(cover_small_url.replace('https://www.javbus.com/imgs/thumbs/', '')) == 7:
                image_download = True
            else:
                cover_small_url = ''    # 非一本道的无码/欧美影片，清空小图地址，因为小图都是未裁剪的低分辨率图片
        runtime = getRuntime(html_info)
        studio = getStudio(html_info)
        publisher = getPublisher(html_info, studio)
        director = getDirector(html_info)
        series = getSeries(html_info)
        extrafanart = getExtraFanart(html_info, 'https://www.javbus.com')
        if 'KMHRS' in number:   # 剧照第一张是高清图
            image_download = True
            if extrafanart:
                cover_small_url = extrafanart[0]
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
                'cover_small': cover_small_url,
                'extrafanart': extrafanart,
                'image_download': image_download,
                'image_cut': image_cut,
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


# print(main('KMHRS-050'))    # 小封面图要下载
# print(main('070621_001')) # 小封面图要下载
# print(main('heyzo-1031')) # 小封面图要下载
# print(main('heyzo-0811')) # 小封面图要下载
# print(main('heyzo-1673')) # 小封面图不要下载
# print(main('dv-1175'))    # 有码
# print(main('dv1175'))
# print(main('ssni-644'))
# print(main('010115-001'))
# print(main('ssni644'))
# print(main('BigTitsatWork-17-09-26'))
# print(main('BrazzersExxtra.21.02.01'))
# print(main('KA-001'))
# print(main('012715-793'))


# print(main('ssni-644', "https://www.javbus.com/SSNI-644"))
# print(main('ssni-802', ""))
# print(main('DirtyMasseur.20.07.26', "https://www.javbus.one/DirtyMasseur-20-07-26"))
