from logging import error
import re
from PIL.JpegImagePlugin import convert_dict_qtables
from bs4 import BeautifulSoup, SoupStrainer
from lxml import etree
import json
import cloudscraper
from Function.getHtml import get_html, post_html, get_cookies, get_proxies, get_proxy


def getNumber(html):
    result1 = str(html.xpath('//strong[contains(text(),"番號:")]/../span/a/text()')).strip(
        " ['']").replace('_', '-')
    result2 = str(html.xpath('//strong[contains(text(),"ID:")]/../span/a/text()')).strip(
        " ['']").replace('_', '-')
    return str(result2 + result1).strip('+')

    
def getTitle(html):
    try:
        result = str(html.xpath('/html/body/section/div/h2/strong/text()')).strip(" ['']")
        # web_cache_url = etree.tostring(html,encoding="utf-8").decode() 
        # print(web_cache_url)
        return re.sub('.*\] ', '', result.replace('/', ',').replace('\\xa0', '').replace(' : ', ''))
    except:
        return re.sub('.*\] ', '', result.replace('/', ',').replace('\\xa0', ''))


def getActor(html):
    result1 = str(html.xpath('//strong[text()="演員:"]/../span/strong[@class="symbol female"][last()]/preceding-sibling::a/text()'))
    result2 = str(html.xpath('//strong[text()="Actor(s):"]/../span/strong[@class="symbol female"][last()]/preceding-sibling::a/text()'))
    return result1 + result2


def getActorPhoto(html, log_info, cookies, proxies, timeout): 
    actor_list = html.xpath('//strong[@class="symbol female"][last()]/preceding-sibling::a/text()')
    actor_url_list = html.xpath('//strong[@class="symbol female"][last()]/preceding-sibling::a/@href')
    actor_count = len(actor_list)
    actor_dic = {}
    for i in range(actor_count):
        actor_name =  actor_list[i]
        actor_url =  'https://javdb.com' + actor_url_list[i]
        scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            }
        )  # returns a CloudScraper instance
        try:
            html_search = scraper.get(actor_url, cookies=cookies, proxies=proxies, timeout=timeout).text
        except Exception as error_info:
            log_info += '   >>> JAVDB-请求歌手头像：出错！错误信息：%s\n' % str(error_info)
            error_type = 'timeout'
            raise Exception('JAVDB-请求歌手头像：出错！错误信息：%s\n' % str(error_info))
        html = etree.fromstring(html_search, etree.HTMLParser())
        actor_real_url = html.xpath('//span[@class="avatar"]/@style')
        if actor_real_url:
            actor_real_url = actor_real_url[0].strip(" [''])").replace('background-image: url(', '')
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
    result1 = str(html.xpath('//strong[contains(text(),"日期:")]/../span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Released Date:")]/../span/text()')).strip(" ['']")
    return str(result1 + result2).strip('+')

def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getTag(html):
    result1 = str(html.xpath('//strong[contains(text(),"類別:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Tags:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace(",\\xa0", "").replace("'", "").replace(' ', '').replace(',,',
                                                                                                             '').lstrip(
        ',')

def getCover(html):
    try:
        result = str(html.xpath("//img[@class='video-cover']/@src")[0]).strip(" ['']")
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
        print('Error in javdb.getOutlineScore : ' + str(error_info1))
    return outline, score


def main(number, appoint_url='', log_info='', req_web='', isuncensored=False):
    req_web += '-> javdb '
    cookies = get_cookies('javdb')
    proxies = get_proxies()
    proxy_type, proxy, timeout, retry_count = get_proxy()
    log_info += '   >>> JAVDB-开始使用 javdb 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    url_search = ''
    try: # 捕获主动抛出的异常
        if not real_url:
            # 通过搜索获取real_url
            url_search = 'https://javdb.com/search?q=' + number + '&f=all&locale=zh'
            log_info += '   >>> JAVDB-生成搜索页地址: %s\n' % url_search
            # ========================================================================搜索番号
            scraper = cloudscraper.create_scraper(
                browser={
                    'browser': 'firefox',
                    'platform': 'windows',
                    'mobile': False
                }
            )  # returns a CloudScraper instance
            try:
                html_search = scraper.get(url_search, cookies=cookies, proxies=proxies, timeout=timeout).text
                # result, html_search = get_html('https://javdb9.com/search?q=' + number + '&f=all').replace(u'\xa0', u' ')
            except Exception as error_info:
                log_info += '   >>> JAVDB-请求搜索页：出错！错误信息：%s\n' % str(error_info)
                error_type = 'timeout'
                raise Exception('JAVDB-请求搜索页：出错！错误信息：%s\n' % str(error_info))
            if "The owner of this website has banned your access based on your browser's behaving" in html_search:
                log_info += '   >>> JAVDB-请求搜索页：%s\n' % html_search
                error_type = 'SearchCloudFlare'
                raise Exception('JAVDB-请求搜索页：基於你的異常行為，管理員禁止了你的訪問！')
            html = etree.fromstring(html_search, etree.HTMLParser())
            # print(etree.tostring(html,encoding="utf-8").decode())
            html_title = str(html.xpath('//title/text()')).strip(" ['']")
            if 'Cloudflare' in html_title:
                real_url = ''
                log_info += '   >>> JAVDB-请求搜索页：被 5 秒盾拦截！\n'
                error_type = 'SearchCloudFlare'
                raise Exception('JAVDB-请求搜索页：被 5 秒盾拦截！')
            real_url = html.xpath("//div[@class='uid'][contains(text(), $number)]/../@href", number=number)
            if not real_url:
                real_url = html.xpath("//div[@class='uid'][contains(text(), $number)]/../@href", number=number.upper())
            if not real_url:
                log_info += '   >>> JAVDB-搜索结果页：未匹配到番号！\n'
                error_type = 'Movie data not found'
                raise Exception('JAVDB-搜索结果页：未匹配到番号')
            else:
                real_url = 'https://javdb.com' + real_url[0] + '?locale=zh'
                log_info += '   >>> JAVDB-生成详情页地址：%s\n' % real_url

        if real_url:
            scraper = cloudscraper.CloudScraper()
            try:
                html_info = scraper.get(real_url, cookies=cookies, proxies=proxies, timeout=timeout).text
            except Exception as error_info:
                log_info += '   >>> JAVDB-请求详情页：出错！错误信息：%s\n' % str(error_info)
                error_type = 'timeout'
                raise Exception('JAVDB-请求详情页：出错！错误信息：%s\n' % str(error_info))
            # ========================================================================获取评分、简介
            html_detail = etree.fromstring(html_info, etree.HTMLParser())
            html_title = str(html_detail.xpath('//title/text()')).strip(" ['']")
            if html_title == 'Please Wait... | Cloudflare':
                log_info += '   >>> JAVDB-请求详情页：被 5 秒盾拦截！\n'
                error_type = 'SearchCloudFlare'
                raise Exception('JAVDB-请求详情页：被 5 秒盾拦截！]')
            if '登入' in html_title or 'Sign in' in html_title:
                log_info += '   >>> JAVDB-该番号内容需要登录查看！\n'
                if cookies:
                    log_info += '   >>> JAVDB-Cookie 已失效，请到设置中更新 Cookie！\n'
                else:
                    log_info += '   >>> JAVDB-请到【设置】-【网络设置】中添加 javdb Cookie！\n'
                error_type = 'need login'
                raise Exception('JAVDB-该番号内容需要登录查看！')
            imagecut = 1
            outline = ''
            if isuncensored and (re.match('^\d{4,}', number) or re.match('n\d{4}', number)):  # 无码，收集封面、评分
                imagecut = 0
                score = getScore(html_detail)
            elif 'HEYZO' in number.upper():  # HEYZO，收集封面、评分、简介
                imagecut = 0
                outline, score = getOutlineScore(number)
            else:  # 其他，收集评分、简介
                outline, score = getOutlineScore(number)
                score = getScore(html_detail)
            # ========================================================================收集信息
            actor = getActor(html_detail) # 获取actor
            if len(actor) == 0 and 'FC2-' in number.upper():
                actor.append('FC2-NoActor')
            actor = str(actor).strip(" [',']").replace('\'', '')
            title = getTitle(html_detail) # 获取标题并去掉头尾歌手名
            title = title.replace('中文字幕', '').replace('無碼', '').replace("\\n", '').replace('_','-').replace(number.upper(), '').replace(number, '').strip().replace('--', '-')
            if not title:
                log_info += '   >>> JAVDB- title 获取失败！\n'
                error_type = 'need login'
                raise Exception('JAVDB- title 获取失败！]')
            cover_url = getCover(html_detail) # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> JAVDB- cover url 获取失败！\n'
                error_type = 'Cover Url is None!'
                raise Exception('JAVDB- cover url 获取失败！]')
            if imagecut == 3 and 'http' not in cover_small:
                log_info += '   >>> JAVDB- cover url 获取失败！\n'
                error_type = 'Cover_small Url is None!'
                raise Exception('JAVDB- cover_small url 获取失败！]')
            release = getRelease(html_detail)

            try:
                dic = {
                    'title': title,
                    'number': number.upper(),
                    'actor': actor,
                    'outline': str(outline),
                    'tag': getTag(html_detail),
                    'release': str(release),
                    'year': getYear(release),
                    'runtime': getRuntime(html_detail),
                    'score': str(score),
                    'series': getSeries(html_detail),
                    'director': getDirector(html_detail),
                    'studio': getStudio(html_detail),
                    'publisher': getPublisher(html_detail),
                    'source': 'javdb.main',
                    'website': str(real_url).replace('?locale=zh', '').strip('[]'),
                    'search_url': str(url_search),
                    'actor_photo': getActorPhoto(html_detail, log_info, cookies, proxies, timeout),
                    'cover': str(cover_url),
                    'cover_small': '',
                    'extrafanart': getExtraFanart(html_detail),
                    'imagecut': imagecut,
                    'log_info': str(log_info),
                    'error_type': '',
                    'error_info': str(error_info),
                    'req_web': req_web,
                }
                log_info += '   >>> JAVDB-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> JAVDB-生成数据字典：出错！ 错误信息：%s\n' % str(error_info)
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
# print(main('x-art.19.11.03'))
# print(main('032020-001'))
# print(main('S2M-055'))
# print(main('LUXU-1217'))

# print(main('SSIS-001', ''))
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
