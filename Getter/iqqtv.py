import re
from lxml import etree
import json
from numpy import number
from Function.getHtml import get_html, post_html
import urllib3
urllib3.disable_warnings()
from Getter import javdb
from configparser import RawConfigParser


def getModeLike():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    return config.getint('common', 'main_like')

def getTitle(html):
    result = html.xpath('//p[@class="movie_txt_nsme"]/text()')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getWebNumber(title, number):
    result = title.split(' ')
    if len(result) > 1:
        result = result[-1]
    else:
        result = number.upper()
    return result
    
def getActor(html):
    try:
        result = str(html.xpath('//p[@class="movie_txt_av"]/a/span/text()')).strip("['']").replace("'", '')
    except:
        result = ''
    return result

def getActorPhoto(actor):
    actor = actor.split(',')
    data = {}
    for i in actor:
        actor_photo = {i: ''}
        data.update(actor_photo)
    return data

def getCover(html):
    result = html.xpath('//p[@id="mv_img"]/img/@src')
    if result:
        result = result[0]
    else:
        result = ''
    return result

def getOutline(html):
    result = html.xpath('//p[@itemprop="description"]/span/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result

def getRelease(html):
    result = html.xpath('//p[@itemprop="datePublished"]/text()')
    if result:
        result = result[0].replace('/', '-').strip()
    else:
        result = ''
    return result

def getYear(realse):
    try:
        result = str(re.search('\d{4}', realse).group())
        return result
    except:
        return realse[:4]

def getTag(html):
    result = html.xpath('//p[@class="movie_txt_tag"]/a/text()')
    if result:
        result = str(result).strip(" ['']").replace("'", "").replace(', ', ',')
    else:
        result = ''
    return result

def getMosaic(tag):
    if '无码' in tag or '無碼' in tag or '無修正' in tag:
        mosaic = '无码'
    else:
        mosaic = '有码'
    return mosaic

def getStudio(html):
    result = html.xpath('//p[@class="movie_txt_fac"]/a/span/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result

def getRuntime(html):
    result = html.xpath('//meta[@itemprop="duration"]/@content')
    if result:
        result = result[0].strip().split(':')
        if len(result) == 3:
            result = int(int(result[0])*60 + int(result[1]) + int(result[2])/60)
    else:
        result = ''
    return str(result)

def getPublisher(html):
    result1 = str(html.xpath('//strong[contains(text(),"發行:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Publisher:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')

def getSeries(html):
    result1 = str(html.xpath('//strong[contains(text(),"系列:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Series:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')

def getExtraFanart(html):  # 获取封面链接
    extrafanart_list = html.xpath("//div[@class='tile-images preview-images']/a[@class='tile-item']/@href")
    return extrafanart_list

def getDirector(html):
    result = html.xpath('//span[@itemprop="director"]/text()')
    if result:
        result = result[0].replace('/', '-')
    else:
        result = ''
    return result

def getScore(html):
    result = str(html.xpath("//span[@class='score-stars']/../text()")).strip(" ['']")
    try:
        score = re.findall(r'(\d{1}\..+)分', result)
        if score:
            score = score[0]
        else:
            score = ''
    except:
        score = ''
    return score

def main(number, appoint_url='', translate_language='zh_cn', log_info='', req_web='', isuncensored=False):
    req_web += '-> iqqtv '
    log_info += '   >>> iqqtv-开始使用iqqtv进行刮削\n'
    # number = 'snis-555'
    # number = '070121_001'
    # number = 'bt-191'
    real_url = appoint_url
    iqqtv_domain = 'https://iqqtv.cloud'
    cover_url = ''
    error_type = ''
    error_info = ''
    imagecut = 1
    mosaic = '有码'
    url_search = ''
    if translate_language == 'zh_cn':
        iqqtv_url = 'https://iqqtv.cloud/cn/'
    elif translate_language == 'zh_tw':
        iqqtv_url = 'https://iqqtv.cloud/'
    else:
        iqqtv_url = 'https://iqqtv.cloud/jp/'

    try: # 捕获主动抛出的异常
        if not real_url:
            # 通过搜索获取real_url
            url_search = iqqtv_url + 'search.php?kw=' + number
            log_info += '   >>> iqqtv-生成搜索页地址: %s\n' % url_search
            # ========================================================================搜索番号
            result, html_search = get_html(url_search)
            if not result:
                log_info += '   >>> iqqtv-请求搜索页：错误！信息：' + html_search
                error_type = 'timeout'
                raise Exception('iqqtv-请求搜索页：错误！信息：' + html_search)
            # with open('11.txt', 'wt') as f:
            #     f.write(html_search)
            html = etree.fromstring(html_search, etree.HTMLParser())
            real_url = html.xpath("//h3[@class='one_name ga_name' and (contains(text(), $number)) and not (contains(text(), '克破'))]/../@href", number=number.upper())
            # real_url = html.xpath("//h3[@class='one_name ga_name'][contains(text(), $number)]/../@href", number=number.upper())
            # print(real_url)

            if real_url:
                real_url = iqqtv_domain + real_url[0]
                log_info += '   >>> iqqtv-匹配详情页地址： %s \n' % real_url
            else:
                log_info += '   >>> iqqtv-搜索结果页匹配番号：未匹配到番号！ \n'
                error_type = 'iqqtv-搜索结果页匹配番号：未匹配到番号！'
                raise Exception('iqqtv-搜索结果页匹配番号：未匹配到番号！')
            # print(real_url)

        if real_url:
            try:
                result, html_content = get_html(real_url)
            except Exception as error_info:
                log_info += '   >>> iqqtv-请求详情页：出错！错误信息：%s \n' % str(error_info)
                error_type = 'timeout'
                raise Exception('iqqtv-请求详情页：出错！错误信息：%s \n' % str(error_info))          
            # with open('123.txt', 'wt') as f:
            #     f.write(html_content)
            html_info = etree.fromstring(html_content, etree.HTMLParser())
            title = getTitle(html_info) # 获取标题
            # print(title)
            if not title:
                log_info += '   >>> iqqtv- title 获取失败！ \n'
                error_type = 'iqqtv- title 获取失败！'
                raise Exception('iqqtv- title 获取失败!')
            web_number = getWebNumber(title, number)    # 获取番号，用来替换标题里的番号
            # print(web_number)
            title = title.replace(' %s' % web_number, '').strip()
            # print(title)
            actor = getActor(html_info) # 获取actor
            # print(actor)
            actor_photo = getActorPhoto(actor)
            # print(actor_photo)
            cover_url = getCover(html_info) # 获取cover
            # print(cover_url)
            if 'http' not in cover_url:
                log_info += '   >>> iqqtv- cover url 获取失败！ \n'
                error_type = 'Cover Url is None!'
                raise Exception('iqqtv- cover url 获取失败!')
            outline = getOutline(html_info)
            # print(outline)
            release = getRelease(html_info)
            # print(release)
            year = getYear(release)
            # print(year)
            tag = getTag(html_info)
            # print(tag)
            mosaic = getMosaic(tag)
            if mosaic == '无码':
                imagecut = 3
            # print(mosaic)
            studio = getStudio(html_info)
            # print(studio)
            runtime = getRuntime(html_info)
            # print(runtime)
            score = ''
            series = ''
            director = ''
            publisher = studio
            extrafanart = ''
            mode_like = getModeLike()
            if mode_like:
                json_data = json.loads(javdb.main(number, '', log_info, req_web))
                req_web = json_data['req_web']
                if json_data.get('title'):
                    runtime = json_data['runtime']
                    score = json_data['score']
                    series = json_data['series']
                    director = json_data['director']
                    # publisher = json_data['publisher']
                    # studio = json_data['studio']
                    extrafanart = json_data['extrafanart']
                    actor_photo = json_data['actor_photo'] # 暂时使用javdb的日文名字，避免emby不识别歌手头像
                    if '克破' in title or '克破' in outline:
                        title = json_data['title']
                        outline = json_data['outline']
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
                    'source': 'iqqtv',
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
                log_info += '   >>> iqqtv-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> iqqtv-生成数据字典：出错！ 错误信息：%s \n' % str(error_info)
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


# print(main('abs-141'))
# print(main('HYSD-00083'))
# print(main('IESP-660'))
# print(main('n1403'))
# print(main('GANA-1910'))
# print(main('heyzo-1031'))
# print(main_us('x-art.19.11.03'))
# print(main('032020-001'))
# print(main('S2M-055'))
# print(main('LUXU-1217'))

# print(main('1101132', ''))
# print(main('OFJE-318'))
# print(main('110119-001'))
# print(main('abs-001'))
# print(main('SSIS-090', ''))
# print(main('SSIS-090', ''))
# print(main('SNIS-016', ''))
# print(main('HYSD-00083', ''))
# print(main('IESP-660', ''))
# print(main('n1403', ''))
# print(main('GANA-1910', ''))
# print(main('heyzo-1031', ''))
# print(main_us('x-art.19.11.03'))
# print(main('032020-001', ''))
# print(main('S2M-055', ''))
# print(main('LUXU-1217', ''))
# print(main_us('x-art.19.11.03', ''))
