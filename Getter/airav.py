import sys  # NOQA: E402
sys.path.append('../')  # NOQA: E402
import re
from lxml import etree
import json
from Function.getHtml import get_html
import Function.config as cf
import urllib3
urllib3.disable_warnings()


def getWebNumber(html):
    result = html.xpath(
        '//h5[@class=" d-none d-md-block text-primary mb-3"]/text()')
    if result:
        result = result[0].strip()
    else:
        result = ''
    return result


def getTitle(html):
    result = str(html.xpath(
        '//h5[@class=" d-none d-md-block"]/text()')).strip(" ['']")
    return result


def getActor(html):
    try:
        result = str(html.xpath(
            '//li[@class="videoAvstarListItem"]/a/text()')).strip("['']").replace("'", '')
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


def getStudio(html):
    result = str(html.xpath(
        '//a[contains(@href,"video_factory")]/text()')).strip(" ['']")
    return result


def getRelease(html):
    result = str(html.xpath(
        '//ul[@class="list-unstyled pl-2 "]/li/text()')[-1]).strip(" ['']")
    return result


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getTag(html):
    result = str(html.xpath(
        '//div[@class="tagBtnMargin"]/a/text()')).strip(" ['']").replace("'", "")
    return result


def getCover(html):
    try:
        result = str(html.xpath(
            '//div[@class="videoPlayerMobile d-none "]/div/img/@src')[0]).strip(" ['']")
    except:
        result = ''
    return result


def getOutline(html, translate_language, real_url):
    if translate_language == 'zh_cn':
        real_url = real_url.replace(
            'cn.airav.wiki', 'www.airav.wiki').replace('zh-CN', 'zh-TW')
        try:
            result, html_content = get_html(real_url)
        except Exception as error_info:
            pass
        html = etree.fromstring(html_content, etree.HTMLParser())
    result = str(html.xpath(
        '//div[@class="synopsis"]/p/text()')).strip(" ['']")
    return result


def main(number, appoint_url='', translate_language='zh_cn', log_info='', req_web='', isuncensored=False):
    req_web += '-> airav[%s] ' % translate_language.replace('zh_', '')
    log_info += '   >>> AIRAV-开始使用airav进行刮削\n'
    config = cf.get_config()
    del_actor_name = config.get('del_actor_name')
    number = number.upper()
    if re.match('N\d{4}', number):  # n1403
        number = number.lower()
    real_url = appoint_url
    cover_url = ''
    error_type = ''
    error_info = ''
    image_cut = 'right'
    image_download = False
    url_search = ''
    mosaic = '有码'
    if translate_language == 'zh_cn':
        airav_url = 'https://cn.airav.wiki'
        airav_lan = '?lng=zh-CN'
    elif translate_language == 'zh_tw':
        airav_url = 'https://www.airav.wiki'
        airav_lan = '?lng=zh-TW'
    else:
        airav_url = 'https://jp.airav.wiki'
        airav_lan = '?lng=jp'

    try:  # 捕获主动抛出的异常
        if not real_url:
            # 通过搜索获取real_url
            url_search = airav_url + '/?search=' + number
            log_info += '   >>> AIRAV-生成搜索页地址: %s \n' % url_search
            # ========================================================================搜索番号
            result, html_search = get_html(url_search)
            if not result:
                log_info += '   >>> AIRAV-请求搜索页：错误！信息：' + html_search
                error_type = 'timeout'
                raise Exception('>>> AIRAV-请求搜索页：错误！信息：' + html_search)
            html = etree.fromstring(html_search, etree.HTMLParser())
            real_url = html.xpath(
                "//div[@class='coverImageBox']/img[@class='img-fluid video-item coverImage' and contains(@alt, $number1) and not(contains(@alt, '克破'))]/../../@href", number1=number)

            if real_url:
                real_url = airav_url + real_url[0] + airav_lan
                log_info += '   >>> AIRAV-匹配详情页地址： %s \n' % real_url
            else:
                log_info += '   >>> AIRAV-搜索结果页匹配番号：未匹配到番号！ \n'
                error_type = 'Movie data not found'
                raise Exception('Movie data not found')

        if real_url:
            try:
                result, html_content = get_html(real_url)
            except Exception as error_info:
                log_info += '   >>> AIRAV-请求详情页：出错！错误信息：%s \n' % str(
                    error_info)
                error_type = 'timeout'
                raise Exception('>>> AIRAV-请求详情页：出错！错误信息：%s \n' %
                                str(error_info))
            html_info = etree.fromstring(html_content, etree.HTMLParser())
            title = getTitle(html_info)  # 获取标题
            if not title:
                log_info += '   >>> AIRAV- title 获取失败！ \n'
                error_type = 'AIRAV - title 获取失败！'
                raise Exception('>>> AIRAV- title 获取失败!')
            web_number = getWebNumber(html_info)    # 获取番号，用来替换标题里的番号
            title = title.replace(web_number, '').strip()
            actor = getActor(html_info)  # 获取actor
            actor_photo = getActorPhoto(actor)
            if del_actor_name:
                title = title.replace(' ' + actor, '')
            cover_url = getCover(html_info)  # 获取cover
            if 'http' not in cover_url:
                log_info += '   >>> AIRAV- cover url 获取失败！ \n'
                error_type = 'Cover Url is None!'
                raise Exception('>>> AIRAV- cover url 获取失败!')
            outline = getOutline(html_info, translate_language, real_url)
            release = getRelease(html_info)
            year = getYear(release)
            tag = getTag(html_info)
            studio = getStudio(html_info)
            runtime = ''
            score = ''
            series = ''
            director = ''
            publisher = studio
            extrafanart = ''
            if '无码' in tag or '無修正' in tag or '無码' in tag or 'uncensored' in tag.lower():
                mosaic = '无码'

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
                    'source': 'airav',
                    'website': real_url,
                    'search_url': url_search,
                    'actor_photo': actor_photo,
                    'cover': cover_url,
                    'cover_small': '',
                    'extrafanart': extrafanart,
                    'image_download': image_download,
                    'image_cut': image_cut,
                    'log_info': str(log_info),
                    'error_type': '',
                    'error_info': str(error_info),
                    'req_web': req_web,
                    'mosaic': mosaic,
                }
                log_info += '   >>> AIRAV-数据获取成功！\n'
                dic['log_info'] = log_info
            except Exception as error_info:
                log_info += '   >>> AIRAV-生成数据字典：出错！ 错误信息：%s \n' % str(
                    error_info)
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
    js = json.dumps(dic, ensure_ascii=False, sort_keys=False,
                    indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


if __name__ == '__main__':
    # print(main('PRED-300')) # 马赛克破坏版
    print(main('abs-141'))
    # print(main('HYSD-00083'))
    # print(main('IESP-660'))
    # print(main('n1403'))
    # print(main('GANA-1910'))
    # print(main('heyzo-1031'))
    # print(main('x-art.19.11.03'))
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
