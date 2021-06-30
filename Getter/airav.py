from logging import error
import re
from PIL.JpegImagePlugin import convert_dict_qtables
from bs4 import BeautifulSoup, SoupStrainer
from lxml import etree
import json
import cloudscraper
from requests.api import get

from requests.models import stream_decode_response_unicode
from Function.getHtml import get_html
from Function.getHtml import post_html
import urllib3
urllib3.disable_warnings()
from Getter import  javdb

def getNumber(html):
    result1 = str(html.xpath('//strong[contains(text(),"番號:")]/../span/a/text()')).strip(
        " ['']").replace('_', '-')
    result2 = str(html.xpath('//strong[contains(text(),"ID:")]/../span/a/text()')).strip(
        " ['']").replace('_', '-')
    return str(result2 + result1).strip('+')

    
def getTitle(html):
    result = str(html.xpath('//h5[@class=" d-none d-md-block"]/text()')).strip(" ['']")
    return result


def getActor(html):
    try:
        result = str(html.xpath('//li[@class="videoAvstarListItem"]/a/text()')).strip("['']").replace("'", '')
    except:
        result = ''
    return result


def getActorPhoto(html, airav_url, log_info): 
    actor_list = html.xpath('//li[@class="videoAvstarListItem"]/a/text()')
    actor_url_list = html.xpath('//li[@class="videoAvstarListItem"]/a/@href')
    actor_count = len(actor_list)
    actor_dic = {}
    for i in range(actor_count):
        actor_name =  actor_list[i]
        actor_url =  airav_url + actor_url_list[i]
        try:
            result, html_content = get_html(actor_url)
        except Exception as error_info:
            log_info += '   >>> AIRAV请求歌手头像：出错！错误信息：%s\n' % str(error_info)
            error_type = 'timeout'
            raise Exception('AIRAV请求歌手头像：出错！错误信息：%s\n' % str(error_info))
        html = etree.fromstring(html_content, etree.HTMLParser())
        # web_cache_url = etree.tostring(html,encoding="utf-8").decode() # 将element对象转化为字符串
        # print(web_cache_url)
        # with open('12.txt', 'wt') as f:
        #     f.write(web_cache_url)        
        actor_real_url = html.xpath('//div[@class="image-gallery-slide  center "]/div/img[@class="image-gallery-image"]/@src')
        if actor_real_url:
            actor_real_url = actor_real_url[0]
        else:
            actor_real_url = ''
        dic = {actor_name : actor_real_url}
        actor_dic.update(dic)
    return actor_dic


def getStudio(html):
    result1 = str(html.xpath('//strong[contains(text(),"片商:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Maker:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getPublisher(html):
    result1 = str(html.xpath('//strong[contains(text(),"發行:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Publisher:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getRuntime(html):
    result1 = str(html.xpath('//strong[contains(text(),"時長")]/../span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Duration:")]/../span/text()')).strip(" ['']")
    return str(result1 + result2).replace(' 分鍾', '').replace(' minute(s)', '')


def getSeries(html):
    result1 = str(html.xpath('//strong[contains(text(),"系列:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Series:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')

def getRelease(html):
    result = str(html.xpath('//ul[@class="list-unstyled pl-2 "]/li/text()')[-1]).strip(" ['']")
    return result

def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getTag(html):
    result = str(html.xpath('//div[@class="tagBtnMargin"]/a/text()')).strip(" ['']").replace("'", "")
    return result

def getCover(html):
    try:
        result = str(html.xpath('//div[@class="videoPlayerMobile d-none "]/div/img/@src')[0]).strip(" ['']")
    except:
        result = ''
    return result


def getExtraFanart(html):  # 获取封面链接
    extrafanart_list = html.xpath("//div[@class='tile-images preview-images']/a[@class='tile-item']/@href")
    return extrafanart_list

def getDirector(html):
    result1 = str(html.xpath('//strong[contains(text(),"導演:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Director:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


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

def getOutline(html, translate_language, real_url):
    if translate_language == 'zh_cn':
        real_url = real_url.replace('cn.airav.wiki', 'www.airav.wiki').replace('zh-CN', 'zh-TW')
        try:
            result, html_content = get_html(real_url)
        except Exception as error_info:
            pass
        html = etree.fromstring(html_content, etree.HTMLParser())
    result = str(html.xpath('//div[@class="synopsis"]/p/text()')).strip(" ['']")
    return result

def getOutlineScore(number):  # 获取简介
    outline = ''
    score = ''
    try:
        result, response = post_html("https://www.jav321.com/search", query={"sn": number})
        detail_page = etree.fromstring(response, etree.HTMLParser())
        outline = str(detail_page.xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/div/text()')).strip(" ['']")
        if re.search(r'<b>评分</b>: <img data-original="/img/(\d+).gif" />', response):
            score = re.findall(r'<b>评分</b>: <img data-original="/img/(\d+).gif" />', response)[0]
            score = str(float(score) / 10.0)
        else:
            score = str(re.findall(r'<b>评分</b>: ([^<]+)<br>', response)).strip(" [',']").replace('\'', '')
        if outline == '':
            result, dmm_htmlcode = get_html(
                "https://www.dmm.co.jp/search/=/searchstr=" + number.replace('-', '') + "/sort=ranking/")
            if 'に一致する商品は見つかりませんでした' not in dmm_htmlcode:
                dmm_page = etree.fromstring(dmm_htmlcode, etree.HTMLParser())
                url_detail = str(dmm_page.xpath('//*[@id="list"]/li[1]/div/p[2]/a/@href')).split(',', 1)[0].strip(
                    " ['']")
                if url_detail != '':
                    result, dmm_detail = get_html(url_detail)
                    html = etree.fromstring(dmm_detail, etree.HTMLParser())
                    outline = str(html.xpath('//*[@class="mg-t0 mg-b20"]/text()')).strip(" ['']").replace('\\n', '').replace('\n', '')
    except Exception as error_info1:
        print('Error in airav.getOutlineScore : ' + str(error_info1))
    return outline, score


def main(number, appoint_url='', translate_language='zh_cn', log_info='', isuncensored=False):
    log_info += '   >>> AIRAV-开始使用airav进行刮削\n'
    number = number.upper()
    real_url = appoint_url
    airav_url = 'https://cn.airav.wiki'
    airav_lan = '?lng=zh-CN'
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    imagecut = 1
    url_search = ''
    if translate_language == 'zh_cn':
        airav_url = 'https://cn.airav.wiki'
        airav_lan = '?lng=zh-CN'
    elif translate_language == 'zh_tw':
        airav_url = 'https://www.airav.wiki'
        airav_lan = '?lng=zh-TW'
    else:
        airav_url = 'https://jp.airav.wiki'
        airav_lan = '?lng=jp'      

    try: # 捕获主动抛出的异常
        if not real_url:
            # 通过搜索获取real_url
            url_search = airav_url + '/?search=' + number
            log_info += '   >>> AIRAV-生成搜索页地址: %s\n' % url_search
            # ========================================================================搜索番号
            result, html_search = get_html(url_search)
            if result == 'error':
                log_info += '   >>> AIRAV-请求搜索页：错误！信息：' + html_search
                error_type = 'timeout'
                raise Exception('>>> AIRAV-请求搜索页：错误！信息：' + html_search)
            html = etree.fromstring(html_search, etree.HTMLParser())
            # web_cache_url = etree.tostring(html,encoding="utf-8").decode() # 将element对象转化为字符串
            # print(web_cache_url)
            # with open('11.txt', 'wt') as f:
            #     f.write(web_cache_url)
            real_url = html.xpath("//a[contains(@href, $number)]/@href", number='/' + number)

            if real_url:
                real_url = airav_url + real_url[0] + airav_lan
                imagecut = 1
            else:
                real_url = html.xpath("//a[contains(@href, $number)]/@href", number=number)
                if real_url:
                    real_url = airav_url + real_url[0] + airav_lan
                    imagecut = 3
            if real_url:
                log_info += '   >>> AIRAV-匹配详情页地址： %s \n' % real_url
            else:
                log_info += '   >>> AIRAV-搜索结果页匹配番号：未匹配到番号！ \n'
                error_type = 'Movie not found'
                raise Exception('Movie not found')

        if real_url:
            try:
                result, html_content = get_html(real_url)
            except Exception as error_info:
                log_info += '   >>> AIRAV-请求详情页：出错！错误信息：%s \n' % str(error_info)
                error_type = 'timeout'
                raise Exception('>>> AIRAV-请求详情页：出错！错误信息：%s \n' % str(error_info))          
            html_info = etree.fromstring(html_content, etree.HTMLParser())
            web_cache_url = etree.tostring(html_info,encoding="utf-8").decode() # 将element对象转化为字符串
            # print(web_cache_url)
            # with open('11.txt', 'wt') as f:
            #     f.write(web_cache_url)
            if not title:
                title = getTitle(html_info) # 获取标题
            if not title:
                log_info += '   >>> AIRAV- title 获取失败！ \n'
                error_type = 'AIRAV - title 获取失败！'
                raise Exception('>>> AIRAV- title 获取失败!')
            cover_url = getCover(html_info) # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> AIRAV- cover url 获取失败！ \n'
                error_type = 'Cover Url is None!'
                raise Exception('>>> AIRAV- cover url 获取失败!')
            actor = getActor(html_info) # 获取actor
            title = title.replace(' ' + actor,'').replace(number, '').replace(' ', '').strip()
            # actor_photo = getActorPhoto(html_info, airav_url, log_info) # 歌手头像已可以刮削，但目前没用到，暂时注释掉
            actor_photo = ''
            outline = getOutline(html_info, translate_language, real_url)
            release = getRelease(html_info)
            year = getYear(release)
            tag = getTag(html_info)
            json_data = json.loads(javdb.main(number, '', log_info))
            if json_data.get('title'):
                runtime = json_data['runtime']
                score = json_data['score']
                series = json_data['series']
                director = json_data['director']
                publisher = json_data['publisher']
                studio = json_data['studio']
                extrafanart = json_data['extrafanart']
                publisher = json_data['publisher']
                if '克破' in title:
                    title = json_data['title']
                    outline = json_data['outline']

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
                    'publisher': publisher,
                    'studio': studio,
                    'source': 'airav.main',
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
                }
                log_info += '   >>> AIRAV-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> AIRAV-生成数据字典：出错！ 错误信息：%s \n' % str(error_info)
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


'''
print(main('abs-141'))
print(main('HYSD-00083'))
print(main('IESP-660'))
print(main('n1403'))
print(main('GANA-1910'))
print(main('heyzo-1031'))
print(main_us('x-art.19.11.03'))
print(main('032020-001'))
print(main('S2M-055'))
print(main('LUXU-1217'))
'''

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
