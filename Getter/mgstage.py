import re
from lxml import etree
import json
from Function.getHtml import get_html
import urllib3
urllib3.disable_warnings()

def getTitle(html):
    try:
        result = str(html.xpath('//*[@id="center_column"]/div[1]/h1/text()')).strip(" ['']")
        return result.replace('/', ',')
    except:
        return ''

def getActor(html):
    result = str(html.xpath('//th[contains(text(),"出演")]/../td/a/text()')).replace('\\n', '').strip(" ['']").replace('/', ',').replace('\'', '').replace(' ', '')
    if not result:
        result = str(html.xpath('//th[contains(text(),"出演")]/../td/text()')).replace('\\n', '').strip(" ['']").replace('/', ',').replace('\'', '').replace(' ', '')
    return result

def getActorPhoto(actor):
    d = {}
    for i in actor:
        if ',' not in i or ')' in i:
            p = {i: ''}
            d.update(p)
    return d

def getStudio(html):
    result1 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')

def getPublisher(html):
    result1 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')

def getRuntime(html):
    result1 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).rstrip('min').replace('\'', '').replace(' ', '').replace('\\n', '')

def getSeries(html):
    result1 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')

def getNum(html):
    result1 = str(html.xpath('//th[contains(text(),"品番：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"品番：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')

def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease

def getRelease(html):
    result1 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')

def getTag(html):
    result1 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')

def getCoverSmall(cover_url):
    result = cover_url.replace('/pb_', '/pf_')
    return result

def getCover(html):
    result = str(html.xpath('//a[@id="EnlargeImage"]/@href')).strip(" ['']")
    return result

def getExtraFanart(html):  # 获取封面链接
    extrafanart_list = html.xpath("//dl[@id='sample-photo']/dd/ul/li/a[@class='sample_image']/@href")
    return extrafanart_list

def getOutline(html):
    result = str(html.xpath('//*[@id="introduction"]/dd/p[1]/text()')).strip(" ['']")
    return result

def getScore(html):
    result = html.xpath('//td[@class="review"]/span/@class')
    if result:
        result = '%.1f' % (int(result[0].replace('star_', '')[:2]) / 10)
    return str(result)

def main(number, appoint_url='', log_info='', req_web=''):
    req_web += '-> mgstage '
    log_info += '   >>> MGSTAGE-开始使用 mgstage 进行刮削\n'
    real_url = appoint_url
    title = ''
    cover_url = ''
    cover_small = ''
    error_type = ''
    error_info = ''
    dic = {}

    try:
        number = number.upper()
        url = 'https://www.mgstage.com/product/product_detail/' + str(number) + '/'
        if appoint_url != '':
            url = appoint_url
        result, htmlcode = get_html(url, cookies={'adc': '1'})
        if not result:
            log_info += '   >>> MGSTAGE-请求详情页：错误！信息：' + htmlcode
            error_type = 'timeout'
            raise Exception('>>> MGSTAGE-请求详情页：错误！信息：' + htmlcode)
        if not htmlcode.strip():
            log_info += '   >>> MGSTAGE-请检查代理设置！'
            error_type = 'timeout'
            raise Exception('MGSTAGE-请检查代理设置!')            
        htmlcode = htmlcode.replace('ahref', 'a href')  # 针对a标签、属性中间未分开
        htmlcode = etree.fromstring(htmlcode, etree.HTMLParser())
        actor = getActor(htmlcode).replace(' ', '').strip(',')
        title = getTitle(htmlcode).replace("\\n", '').replace('        ', '').strip(',').strip() # 获取标题
        if not title:
            log_info += '   >>> MGSTAGE-找不到该番号数据！ \n'
            error_type = '找不到该番号数据'
            raise Exception('MGSTAGE-找不到该番号数据！')
        cover_url = getCover(htmlcode) # 获取cover
        cover_small_url = getCoverSmall(cover_url) # 获取cover
        if 'http' not in cover_url:
            log_info += '   >>> MGSTAGE-Cover Url is none! \n'
            error_type = 'Cover Url is None!'
            raise Exception('MGSTAGE-Cover Url is none!')
        outline = getOutline(htmlcode).replace('\n', '').strip(',')
        release = getRelease(htmlcode).strip(',').replace('/', '-')
        tag = getTag(htmlcode).strip(',')
        year = getYear(release).strip(',')
        runtime = getRuntime(htmlcode).strip(',')
        score = getScore(htmlcode).strip(',')
        series = getSeries(htmlcode).strip(',')
        studio = getStudio(htmlcode).strip(',')
        publisher = getPublisher(htmlcode).strip(',')
        actor_photo= getActorPhoto(actor.split(','))
        extrafanart = getExtraFanart(htmlcode)
        try:
            dic = {
                'title': str(title),
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
                'publisher': publisher,
                'source': 'mgstage.main',
                'website': url,
                'actor_photo': actor_photo,
                'cover': str(cover_url),
                'cover_small': cover_small_url,
                'extrafanart':extrafanart,
                'imagecut': 0,
                'log_info': str(log_info),
                'error_type': '',
                'error_info': str(error_info),
                'req_web': req_web,
            }

            log_info += '   >>> MGSTAGE-数据获取成功！\n'
            dic['log_info'] = log_info
        except Exception as error_info:
            log_info += '   >>> MGSTAGE-生成数据字典：出错！ 错误信息：%s\n' % str(error_info)
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


# print(main('300MIUM-382', ''))
# print(main('345SIMM-653'))
# print(main('SIRO-4605'))
# print(main('200GANA-2240'))
# print(main('200GANA-2240'))
# print(main('SIRO-4042'))
# print(main('300MIUM-382'))
# print(main('383reiw-043', ''))
# print(main('300MIUM-382', 'https://www.mgstage.com/product/product_detail/300MIUM-382/'))
