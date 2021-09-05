import re
from PyQt5.QtCore import reset
from lxml import etree
import json
import cloudscraper
from Function.getHtml import get_html, post_html, get_cookies, get_proxies, get_proxy
import urllib3
urllib3.disable_warnings()


def getNumber(html, number):
    result = html.xpath('//a[@class="button is-white copy-to-clipboard"]/@data-clipboard-text')
    if result:
        result = result[0]
    else:
        result = number
    return result

    
def getTitle(html):
    try:
        result = str(html.xpath('/html/body/section/div/h2/strong/text()')).strip(" ['']")
        # web_cache_url = etree.tostring(html,encoding="utf-8").decode() 
        # print(web_cache_url)
        return re.sub('.*\] ', '', result.replace('/', ',').replace('\\xa0', '').replace(' : ', ''))
    except:
        return re.sub('.*\] ', '', result.replace('/', ',').replace('\\xa0', ''))


def getActor(html):
    result = html.xpath('//div[@class="panel-block"]/span[@class="value"]/strong[@class="symbol female"][last()]/preceding-sibling::a/text()')
    actor = ''
    for each in result:
        actor = actor + ',' + each.strip()
    return actor

def getActorPhoto(actor):
    actor = actor.split(',')
    data = {}
    for i in actor:
        actor_photo = {i: ''}
        data.update(actor_photo)
    return data

def getActorPhoto2(html, log_info, cookies, proxies, timeout): 
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

def getMosaic(title, isuncensored):
    if '無碼' in title or 'Uncensored' in title or isuncensored:
        mosaic = '无码'
    else:
        mosaic = '有码'
    return mosaic

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

def getRealUrl(html, number):  # 获取详情页链接
    url_list = html.xpath("//a[@class='box']/@href")
    if '.' in number:
        old_date = re.findall('\.\d+\.\d+\.\d+', number)
        if old_date:
            old_date = old_date[0]
            new_date = '.20' + old_date[1:]
            number = number.replace(old_date, new_date)
    for each in url_list:
        text_list = html.xpath("//a[@href=$url]/div/text()", url=each)
        text_list = str(text_list).replace("', '", '').replace(' ', '').replace('\\n', '').replace('-', '').replace('.', '')
        if number.upper().replace('.', '').replace('-', '') in text_list.upper():
            return each
    return False

def getCoverSmall(number, real_url):
    a = real_url.replace('/v/', '')[:2].lower()
    result = 'https://jdbimgs.com/thumbs/' + a + real_url.replace('/v/', '/') + '.jpg'
    if re.findall('\.\d+\.\d+\.\d+', number):
        result = ''
    return result

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
            except Exception as error_info:
                log_info += '   >>> JAVDB-请求搜索页：出错！错误信息：%s\n' % str(error_info)
                error_type = 'timeout'
                raise Exception('JAVDB-请求搜索页：出错！错误信息：%s\n' % str(error_info))
            if "The owner of this website has banned your access based on your browser's behaving" in html_search:
                log_info += '   >>> JAVDB-请求搜索页：%s \n' % html_search
                error_type = 'SearchCloudFlare'
                raise Exception('JAVDB-请求搜索页：基於你的異常行為，管理員禁止了你的訪問！')
            html = etree.fromstring(html_search, etree.HTMLParser())
            html_title = str(html.xpath('//title/text()')).strip(" ['']")
            if 'Cloudflare' in html_title:
                real_url = ''
                log_info += '   >>> JAVDB-请求搜索页：被 5 秒盾拦截！\n'
                error_type = 'SearchCloudFlare'
                raise Exception('JAVDB-请求搜索页：被 5 秒盾拦截！')
            real_url = getRealUrl(html, number)
            if not real_url:
                log_info += '   >>> JAVDB-搜索结果页：未匹配到番号！\n'
                error_type = 'Movie data not found'
                raise Exception('JAVDB-搜索结果页：未匹配到番号')
            else:
                cover_small = getCoverSmall(number, real_url)
                real_url = 'https://javdb.com' + real_url + '?locale=zh'
                log_info += '   >>> JAVDB-生成详情页地址：%s \n' % real_url

        if real_url:
            scraper = cloudscraper.CloudScraper()
            try:
                html_info = scraper.get(real_url, cookies=cookies, proxies=proxies, timeout=timeout).text
            except Exception as error_info:
                log_info += '   >>> JAVDB-请求详情页：出错！错误信息：%s\n' % str(error_info)
                error_type = 'timeout'
                raise Exception('JAVDB-请求详情页：出错！错误信息：%s\n' % str(error_info))
            html_detail = etree.fromstring(html_info, etree.HTMLParser())
            html_title = str(html_detail.xpath('//title/text()')).strip(" ['']")
            if html_title == 'Please Wait... | Cloudflare':
                log_info += '   >>> JAVDB-请求详情页：被 5 秒盾拦截！\n'
                error_type = 'SearchCloudFlare'
                raise Exception('JAVDB-请求详情页：被 5 秒盾拦截！')
            if '登入' in html_title or 'Sign in' in html_title:
                log_info += '   >>> JAVDB-该番号内容需要登录查看！\n'
                if cookies:
                    log_info += '   >>> JAVDB-Cookie 已失效，请到设置中更新 Cookie！\n'
                else:
                    log_info += '   >>> JAVDB-请到【设置】-【网络设置】中添加 javdb Cookie！\n'
                error_type = 'need login'
                raise Exception('JAVDB-该番号内容需要登录查看！')
            outline = ''
            imagecut = 1
            if isuncensored:
                imagecut = 3
                if cover_small == '':
                    imagecut = 0
            # ========================================================================收集信息
            actor = getActor(html_detail) # 获取actor
            actor = str(actor).strip(" [',']").replace('\'', '')
            actor_photo = getActorPhoto(actor)
            number = getNumber(html_detail, number)
            title = getTitle(html_detail) # 获取标题并去掉头尾歌手名
            if not title:
                log_info += '   >>> JAVDB- title 获取失败！\n'
                error_type = 'need login'
                raise Exception('JAVDB- title 获取失败！')
            mosaic = getMosaic(title, isuncensored)
            title = title.replace('中文字幕', '').replace('無碼', '').replace("\\n", '').replace('_','-').replace(number.upper(), '').replace(number, '').replace('--', '-').strip()
            cover_url = getCover(html_detail) # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> JAVDB- cover url 获取失败！\n'
                error_type = 'Cover Url is None!'
                raise Exception('JAVDB- cover url 获取失败！')
            release = getRelease(html_detail)
            score = getScore(html_detail)

            try:
                dic = {
                    'title': title,
                    'number': number,
                    'actor': actor,
                    'outline': outline,
                    'tag': getTag(html_detail),
                    'release': str(release),
                    'year': getYear(release),
                    'runtime': getRuntime(html_detail),
                    'score': str(score),
                    'series': getSeries(html_detail),
                    'director': getDirector(html_detail),
                    'studio': getStudio(html_detail),
                    'publisher': getPublisher(html_detail),
                    'source': 'javdb',
                    'website': str(real_url).replace('?locale=zh', '').strip('[]'),
                    'search_url': str(url_search),
                    'actor_photo': actor_photo,
                    'cover': str(cover_url),
                    'cover_small': cover_small,
                    'extrafanart': getExtraFanart(html_detail),
                    'imagecut': imagecut,
                    'log_info': str(log_info),
                    'error_type': '',
                    'error_info': str(error_info),
                    'req_web': req_web,
                    'mosaic': mosaic,
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



# print(main('SIRO-4042'))
# print(main('snis-035'))
# print(main('vixen.18.07.18', ''))
# print(main('vixen.16.08.02', ''))
# print(main('SNIS-016', ''))
# print(main('bangbros18.19.09.17'))
# print(main('x-art.19.11.03'))
# print(main('abs-141'))
# print(main('HYSD-00083'))
# print(main('IESP-660'))
# print(main('n1403'))
# print(main('GANA-1910'))
# print(main('heyzo-1031'))
# print(main('032020-001'))
# print(main('S2M-055'))
# print(main('LUXU-1217'))

# print(main('SSIS-001', ''))
# print(main('SSIS-090', ''))
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
