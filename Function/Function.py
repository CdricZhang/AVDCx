#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logging import log
from random import randint
import time
import re
import os
import json
from PIL import Image
from configparser import RawConfigParser
from Getter import iqqtv_new, javbus, javdb, jav321, dmm, javlibrary_new, avsox, xcity, mgstage, fc2, fc2club, fc2hub, airav


# ========================================================================补全字段判断缺失字段
def getTheData(json_data_more, json_data, flag_suren=False):
    json_data['req_web'] = json_data_more['req_web']
    json_data['log_info'] = json_data_more['log_info']
    # 原json_data无数据
    if not getDataState(json_data):
        return json_data_more
    # 补全网站未刮削到内容
    if not getDataState(json_data_more):
        return json_data
    # 补全网站刮削到内容
    if not json_data['actor'] or json_data['actor'] == '素人' or flag_suren:
        json_data['actor'] = json_data_more['actor']
        json_data['actor_photo'] = json_data_more['actor_photo']
    if not json_data['outline']:
        json_data['outline'] = json_data_more['outline']
    if not json_data['tag']:
        json_data['tag'] = json_data_more['tag']
    if not json_data['release']:
        json_data['release'] = json_data_more['release']
    if not json_data['year']:
        json_data['year'] = json_data_more['year']
    if not json_data['runtime']:
        json_data['runtime'] = json_data_more['runtime']
    if not json_data['score']:
        json_data['score'] = json_data_more['score']
    if not json_data['series']:
        json_data['series'] = json_data_more['series']
    if not json_data['director']:
        json_data['director'] = json_data_more['director']
    if not json_data['studio']:
        json_data['studio'] = json_data_more['studio']
    if not json_data['publisher']:
        json_data['publisher'] = json_data_more['publisher']
    if not json_data['cover_small']:
        json_data['cover_small'] = json_data_more['cover_small']
    if flag_suren and json_data['cover_small']: # 如果是素人，且有小图，则改成下载poster
        json_data['imagecut'] = 3
    if not json_data['extrafanart']:
        json_data['extrafanart'] = json_data_more['extrafanart']
    try:
        if json_data_more['mosaic']:
            json_data['mosaic'] = json_data_more['mosaic']
    except:
        pass
    return json_data


# ========================================================================补全字段
def getMoreData(number, appoint_url, config, json_data):
    main_like = config.getint('common', 'main_like')
    more_website = config.get('common', 'more_website')
    req_web = json_data['req_web']
    log_info = json_data['log_info']
    flag_suren = False
    # 未开启偏好字段 or 未勾选补全网站
    if not main_like or not more_website:
        return json_data
    # 提取类似259luxu-1111素人番号，使用javdb的演员名字替换
    if re.search('\d{2,}[a-zA-Z]{2,}-\d{3,}', number) or 'SIRO' in number.upper():
        number = re.search('[a-zA-Z]+-\d+', number).group()
        flag_suren = True
    # 使用网站补全
    if 'javdb' in more_website and 'javdb' not in req_web:
        json_data_more = json.loads(javdb.main(number, appoint_url, log_info, req_web))
        json_data = getTheData(json_data_more, json_data, flag_suren)
        req_web = json_data['req_web']
        log_info = json_data['log_info']
    if 'jav321' in more_website and 'jav321' not in req_web:
        json_data_more = json.loads(jav321.main(number, appoint_url, log_info, req_web))
        json_data = getTheData(json_data_more, json_data)
        req_web = json_data['req_web']
        log_info = json_data['log_info']
    if 'dmm' in more_website and 'dmm' not in req_web:
        json_data_more = json.loads(dmm.main(number, appoint_url, log_info, req_web))
        json_data = getTheData(json_data_more, json_data)
    return json_data


# ========================================================================是否为无码
def is_uncensored(number):
    if re.match('^\d{4,}', number) or re.match('n\d{4}', number) or 'HEYZO' in number.upper() or re.search('[^.]+\.\d{2}\.\d{2}\.\d{2}', number):
        return True
    else:
        return False


# ========================================================================元数据获取失败检测
def getDataState(json_data):
    if json_data['title'] == '' or json_data['title'] == 'None' or json_data['title'] == 'null':
        return False
    else:
        return True

# ========================================================================去掉异常字符（目前没有在用）
def escapePath(path, Config):  # Remove escape literals
    escapeLiterals = Config['escape']['literals']
    backslash = '\\'
    for literal in escapeLiterals:
        path = path.replace(backslash + literal, '')
    return path


# ========================================================================获取视频列表
def movie_lists(escape_folder, movie_type, movie_path):
    if escape_folder != '':
        escape_folder = re.split('[,，]', escape_folder)
    total = []
    file_type = movie_type.split('|')
    file_root = movie_path.replace('\\', '/')
    for root, dirs, files in os.walk(file_root):
        if escape_folder != '':
            flag_escape = 0
            root = root.replace('\\', '/') + '/'
            for folder in escape_folder:
                if folder in root:
                    flag_escape = 1
                    break
            if flag_escape == 1:
                continue
        for f in files:
            file_name, file_type_current = os.path.splitext(f)
            if re.search(r'^\..+', file_name):
                continue
            if file_type_current.lower() in file_type:
                path = os.path.join(root, f)
                # path = path.replace(file_root, '.')
                path = path.replace("\\\\", "/").replace("\\", "/")
                total.append(path)
    return total


# ========================================================================获取番号
def getNumber(filepath, escape_string):
    filepath = filepath.upper()
    filename = os.path.splitext(os.path.split(filepath)[1])[0]
    # 排除多余字符
    escape_string_list = re.split('[,，]', escape_string)
    for string in escape_string_list:
        filename = filename.replace(string.upper(), '')
    # 再次排除多余字符
    filename = filename.replace('-C.', '.').replace('.PART', '-CD').replace(' ', '-')
    filename = filename.replace('HEYDOUGA-', '').replace('HEYDOUGA', '').replace('CARIBBEANCOM', '').replace('CARIB', '').replace('1PONDO', '').replace('1PON', '').replace('PACOMA', '').replace('PACO', '').replace('10MUSUME', '').replace('-10MU', '').replace('FC2PPV', 'FC2-').replace('--', '-')
    part = ''
    if re.search('-CD\d+', filename):
        part = re.findall('-CD\d+', filename)[0]
    filename = filename.replace(part, '')
    filename = str(re.sub("-\d{4}-\d{1,2}-\d{1,2}", "", filename))  # 去除文件名中时间
    filename = str(re.sub("\d{4}-\d{1,2}-\d{1,2}-", "", filename))  # 去除文件名中时间
    if re.search('[^.]+\.\d{2}\.\d{2}\.\d{2}', filename):  # 提取欧美番号 sexart.11.11.11
        try:
            file_number = re.search('[^.]+\.\d{2}\.\d{2}\.\d{2}', filename).group()
            return file_number.lower()
        except:
            return filename.lower()
    elif re.search('XXX-AV-\d{4,}', filename):  # 提取xxx-av-11111
        file_number = re.search('XXX-AV-\d{4,}', filename).group()
        return file_number
    elif '-' in filename or '_' in filename:  # 普通提取番号 主要处理包含减号-和_的番号
        if 'FC2' in filename:
            filename = filename.replace('PPV', '').replace('_', '-').replace('--', '-')
            if re.search('FC2-\d{5,}', filename):  # 提取类似fc2-111111番号
                file_number = re.search('FC2-\d{5,}', filename).group()
        elif re.search('[a-zA-Z]+-\d+', filename):  # 提取类似mkbd-120番号
            file_number = re.search('\w+-\d+', filename).group()
        elif re.search('\d+[a-zA-Z]+-\d+', filename):  # 提取类似259luxu-1111番号
            file_number = re.search('\d+[a-zA-Z]+-\d+', filename).group()
        elif re.search('[a-zA-Z]+-[a-zA-Z]\d+', filename):  # 提取类似mkbd-s120番号
            file_number = re.search('[a-zA-Z]+-[a-zA-Z]\d+', filename).group()
        elif re.search('\d+-[a-zA-Z]+', filename):  # 提取类似 111111-MMMM 番号
            file_number = re.search('\d+-[a-zA-Z]+', filename).group()
        elif re.search('\d+-\d+', filename):  # 提取类似 111111-000 番号
            file_number = re.search('\d+-\d+', filename).group()
        elif re.search('\d+_\d+', filename):  # 提取类似 111111_000 番号
            file_number = re.search('\d+_\d+', filename).group()
        else:
            file_number = filename
        return file_number
    elif re.search('[A-Z]{3,}00\d{3}', filename):  # 提取ssni00644
        file_number = re.search('[A-Z]{3,}00\d{3}', filename).group()
        file_char = re.search('[A-Z]{3,}', file_number).group()
        a = file_char + '00'
        b = file_char + '-'
        file_number = file_number.replace(a, b)
        return file_number
    elif re.search('N\d{4}', filename):  # 提取N1111
        file_number = re.search('N\d{4}', filename).group()
        return file_number.lower()
    else:  # 提取不含减号-的番号，FANZA CID 保留ssni00644，将MIDE139改成MIDE-139
        try:
            find_num = re.findall(r'\d+', filename)[0]
            find_char = re.findall(r'\D+', filename)[0]
            if len(find_num) <= 4 and len(find_char) > 1:
                file_number = find_char + '-' + find_num
            return file_number
        except:
            return filename


# ========================================================================根据番号获取数据
def getDataFromJSON(file_number, config, website_mode, appoint_url, translate_language):  # 从JSON返回元数据
    # ================================================网站规则添加开始================================================
    isuncensored = is_uncensored(file_number)
    json_data = {}
    if website_mode == 1:  # 从全部网站刮削
        # =======================================================================FC2-111111
        if 'FC2' in file_number.upper():
            file_number = re.search('\d{4,}', file_number).group()
            json_data = json.loads(fc2.main(file_number, appoint_url))
            # if not getDataState(json_data):   # 暂时屏蔽，该网站目前可用
            #     req_web = json_data['req_web']
            #     log_info = json_data['log_info']
            #     json_data = json.loads(fc2club.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(fc2hub.main(file_number, appoint_url, log_info ,req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(avsox.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(airav.main(file_number, appoint_url, translate_language, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javdb.main(file_number, appoint_url, log_info, req_web))
        # =======================================================================sexart.15.06.14
        elif re.search('[^.]+\.\d{2}\.\d{2}\.\d{2}', file_number):
            json_data = json.loads(javdb.main(file_number, appoint_url))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javbus.main(file_number, appoint_url, log_info, req_web))
          # =======================================================================无码抓取:111111-111,n1111,HEYZO-1111,SMD-115
        elif isuncensored:
            json_data = json.loads(iqqtv_new.main(file_number, appoint_url, translate_language))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javbus.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javdb.main(file_number, appoint_url, log_info, req_web, True))
            if not getDataState(json_data) and 'HEYZO' in file_number.upper():
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(jav321.main(file_number, appoint_url, log_info, req_web, True))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(avsox.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(airav.main(file_number, appoint_url, translate_language, log_info, req_web))
        # =======================================================================259LUXU-1111
        elif re.match('\d+[a-zA-Z]+-\d+', file_number) or 'SIRO' in file_number.upper():
            json_data = json.loads(mgstage.main(file_number, appoint_url))
            file_number1 = re.search('[a-zA-Z]+-\d+', file_number).group()
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(jav321.main(file_number1, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javdb.main(file_number1, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javbus.main(file_number1, appoint_url, log_info, req_web))

        # =======================================================================ssni00321
        elif re.match('\D{2,}00\d{3,}', file_number) and '-' not in file_number and '_' not in file_number:
            json_data = json.loads(dmm.main(file_number, appoint_url))
        # =======================================================================MIDE-139
        else:
            json_data = json.loads(iqqtv_new.main(file_number, appoint_url, translate_language))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javbus.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javdb.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(jav321.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(airav.main(file_number, appoint_url, translate_language, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(javlibrary_new.main(file_number, appoint_url, translate_language, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(xcity.main(file_number, appoint_url, log_info, req_web))
            if not getDataState(json_data):
                req_web = json_data['req_web']
                log_info = json_data['log_info']
                json_data = json.loads(avsox.main(file_number, appoint_url, log_info, req_web))
    elif website_mode == 2:  # 仅从iqqtv
        json_data = json.loads(iqqtv_new.main(file_number, appoint_url, translate_language))
    elif website_mode == 3:  # 仅从javbus
        json_data = json.loads(javbus.main(file_number, appoint_url))
    elif website_mode == 4:  # 仅从javdb
        json_data = json.loads(javdb.main(file_number, appoint_url))
    elif website_mode == 5:  # 仅从jav321
        json_data = json.loads(jav321.main(file_number, appoint_url))
    elif website_mode == 6:  # 仅从dmm
        json_data = json.loads(dmm.main(file_number, appoint_url))
    elif website_mode == 7:  # 仅从avsox
        json_data = json.loads(avsox.main(file_number, appoint_url))
    elif website_mode == 8:  # 仅从xcity
        json_data = json.loads(xcity.main(file_number, appoint_url))
    elif website_mode == 9:  # 仅从mgstage
        json_data = json.loads(mgstage.main(file_number, appoint_url))
    elif website_mode == 10:  # 仅从fc2
        json_data = json.loads(fc2.main(file_number, appoint_url))
    elif website_mode == 11:  # 仅从fc2club
        json_data = json.loads(fc2club.main(file_number, appoint_url))
    elif website_mode == 12:  # 仅从fc2hub
        json_data = json.loads(fc2hub.main(file_number, appoint_url))
    elif website_mode == 13:  # 仅从airav
        json_data = json.loads(airav.main(file_number, appoint_url, translate_language))
    elif website_mode == 14:  # 仅从javlibrary
        json_data = json.loads(javlibrary_new.main(file_number, appoint_url, translate_language))
    # ================================================网站规则添加结束================================================
    # ======================================补全字段
    json_data = getMoreData(file_number, appoint_url, config, json_data)

    # ======================================超时或未找到返回
    if json_data['error_type'] or json_data['title'] == '':
        return json_data

    # ======================================处理得到的信息
    title = json_data['title']
    number = json_data['number']
    actor = str(json_data['actor']).strip(" [ ]").replace("'", '').replace(', ', ',').replace('<', '(').replace('>', ')') # 列表转字符串（避免个别网站刮削返回的是列表）
    release = json_data['release']
    try:
        cover_small = json_data['cover_small']
    except:
        cover_small = ''
    tag = str(json_data['tag']).strip(" [ ]").replace("'", '').replace(', ', ',')  #列表转字符串（避免个别网站刮削返回的是列表）

    # ====================================== 去除标题尾巴的演员名
    if config.getint('Name_Rule', 'del_actor_name'):
        title = title.replace((' ' + actor), '')

    # ====================处理异常字符====================== #\/:*?"<>|
    title = title.replace('\\', '')
    title = title.replace('/', '')
    title = title.replace(':', '')
    title = title.replace('*', '')
    title = title.replace('?', '')
    title = title.replace('"', '')
    title = title.replace('<', '')
    title = title.replace('>', '')
    title = title.replace('|', '')
    # title = title.replace(' ', '.')
    # title = title.replace('【', '')
    # title = title.replace('】', '')
    title = title.strip()
    release = release.replace('/', '-').strip('. ')
    try:
        json_data['studio'] = json_data['studio'].strip('. ')
    except:
        pass
    try:
        json_data['publisher'] = json_data['publisher'].strip('. ')
    except:
        pass
    tmpArr = cover_small.split(',')
    if len(tmpArr) > 0:
        cover_small = tmpArr[0].strip('\"').strip('\'')
    for key, value in json_data.items():
        if key == 'title' or key == 'studio' or key == 'director' or key == 'series' or key == 'publisher':
            json_data[key] = str(value).replace('/', '')

    naming_media = config.get('Name_Rule', 'naming_media')
    naming_file = config.get('Name_Rule', 'naming_file')
    folder_name = config.get('Name_Rule', 'folder_name')

    # 返回处理后的json_data
    json_data['title'] = title.replace(u'\xa0', '').replace(u'\u3000', '').replace(u'\u2800', '').strip('. ')
    json_data['number'] = number
    json_data['actor'] = actor.replace(u'\xa0', '').replace(u'\u3000', '').replace(u'\u2800', '').strip('. ')
    json_data['release'] = release
    json_data['cover_small'] = cover_small
    json_data['tag'] = tag
    json_data['naming_media'] = naming_media
    json_data['naming_file'] = naming_file
    json_data['folder_name'] = folder_name
    try:
        json_data['mosaic']
    except:
        json_data['mosaic'] = ''
    finally:
        if not json_data['mosaic']:
            if is_uncensored(number):
                json_data['mosaic'] = '无码'
            else:
                json_data['mosaic']  = '有码'
        print(number, json_data['mosaic'])

    return json_data


# ========================================================================返回json里的数据
def get_info(json_data):
    for key, value in json_data.items():    # 去除unknown
        if str(value).lower() == 'unknown':
            json_data[key] = ''

    title = json_data['title']
    studio = json_data['studio']
    publisher = json_data['publisher']
    year = json_data['year']
    outline = json_data['outline']
    runtime = json_data['runtime']
    director = json_data['director']
    actor_photo = json_data['actor_photo']
    actor = json_data['actor']
    release = json_data['release']
    tag = json_data['tag']
    number = json_data['number']
    cover = json_data['cover']
    website = json_data['website']
    series = json_data['series']
    mosaic = json_data['mosaic']

    return title, studio, publisher, str(year), outline, str(runtime), director, actor_photo, actor, release, tag, number, cover, website, series, mosaic


# ========================================================================保存配置到config.ini
def save_config(json_config):
    config_file = 'config.ini'
    with open(config_file, "wt", encoding='UTF-8') as code:
        print("[modified_time]", file=code)
        print("modified_time = " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), file=code)
        print("", file=code)
        print("[common]", file=code)
        print("main_mode = " + str(json_config['main_mode']), file=code)
        print("main_like = " + str(json_config['main_like']), file=code)
        print("more_website = " + str(json_config['more_website']), file=code)
        print("success_file_move = " + str(json_config['success_file_move']), file=code)
        print("failed_file_move = " + str(json_config['failed_file_move']), file=code)
        print("success_file_rename = " + str(json_config['success_file_rename']), file=code)
        print("soft_link = " + str(json_config['soft_link']), file=code)
        print("show_poster = " + str(json_config['show_poster']), file=code)
        print("translate_language = " + json_config['translate_language'], file=code)
        print("# zh_cn or zh_tw or ja", file=code)
        print("translate_content = " + json_config['translate_content'], file=code)
        print("translate_by = " + json_config['translate_by'], file=code)
        print("# youdao or deepl", file=code)
        print("deepl_key = " + json_config['deepl_key'], file=code)
        print("website = " + json_config['website'], file=code)
        print("# all or iqqtv or javbus or javdb or jav321 or dmm or avsox or xcity or mgstage or fc2 or fc2club or fc2hub or airav or javlibrary", file=code)
        print("series_as_set = " + str(json_config['series_as_set']), file=code)
        print("", file=code)
        print("[proxy]", file=code)
        print("type = " + json_config['type'], file=code)
        print("proxy = " + json_config['proxy'], file=code)
        print("timeout = " + str(json_config['timeout']), file=code)
        print("retry = " + str(json_config['retry']), file=code)
        print("# type: no, http, socks5", file=code)
        print("", file=code)
        print("[Cookies]", file=code)
        print("javdb = " + json_config['javdb'], file=code)
        print("# cookies存在有效期，记得更新", file=code)
        print("", file=code)
        print("[Name_Rule]", file=code)
        print("folder_name = " + json_config['folder_name'], file=code)
        print("naming_media = " + json_config['naming_media'], file=code)
        print("naming_file = " + json_config['naming_file'], file=code)
        print("cnword_char = " + str(json_config['cnword_char']), file=code)
        print("cnword_style = " + str(json_config['cnword_style']), file=code)
        print("folder_cnword = " + str(json_config['folder_cnword']), file=code)
        print("file_cnword = " + str(json_config['file_cnword']), file=code)
        print("del_actor_name = " + str(json_config['del_actor_name']), file=code)
        print("# 命名字段有：title, actor, number, studio, publisher, year, mosaic, runtime, director, release, series", file=code)
        print("", file=code)
        print("[update]", file=code)
        print("update_check = " + str(json_config['update_check']), file=code)
        print("", file=code)
        print("[log]", file=code)
        print("save_log = " + str(json_config['save_log']), file=code)
        print("", file=code)
        print("[media]", file=code)
        print("media_path = " + json_config['media_path'], file=code)
        print("success_output_folder = " + json_config['success_output_folder'], file=code)
        print("failed_output_folder = " + json_config['failed_output_folder'], file=code)
        print("extrafanart_folder = " + str(json_config['extrafanart_folder']), file=code)
        print("media_type = " + json_config['media_type'], file=code)
        print("sub_type = " + json_config['sub_type'], file=code)
        print("", file=code)
        print("[escape]", file=code)
        print("folders = " + json_config['folders'], file=code)
        print("string = " + json_config['string'], file=code)
        print("file_size = " + json_config['file_size'], file=code)
        print("", file=code)
        print("[debug_mode]", file=code)
        print("switch = " + str(json_config['switch_debug']), file=code)
        print("", file=code)
        print("[emby]", file=code)
        print("emby_url = " + json_config['emby_url'], file=code)
        print("api_key = " + json_config['api_key'], file=code)
        print("", file=code)
        print("[mark]", file=code)
        print("poster_mark = " + str(json_config['poster_mark']), file=code)
        print("thumb_mark = " + str(json_config['thumb_mark']), file=code)
        print("mark_size = " + str(json_config['mark_size']), file=code)
        print("mark_type = " + json_config['mark_type'], file=code)
        print("mark_pos = " + json_config['mark_pos'], file=code)
        print("# mark_size : range 1-5", file=code)
        print("# mark_type : sub, leak, uncensored", file=code)
        print("# mark_pos  : bottom_right or bottom_left or top_right or top_left", file=code)
        print("", file=code)
        print("[uncensored]", file=code)
        print("uncensored_poster = " + str(json_config['uncensored_poster']), file=code)
        print("# 0 : official, 1 : cut", file=code)
        print("", file=code)
        print("[file_download]", file=code)
        print("old_poster = " + str(json_config['old_poster']), file=code)
        print("old_thumb = " + str(json_config['old_thumb']), file=code)
        print("old_fanart = " + str(json_config['old_fanart']), file=code)
        print("old_extrafanart = " + str(json_config['old_extrafanart']), file=code)
        print("old_extrafanart_copy = " + str(json_config['old_extrafanart_copy']), file=code)
        print("old_nfo = " + str(json_config['old_nfo']), file=code)
        print("poster = " + str(json_config['poster_download']), file=code)
        print("thumb = " + str(json_config['thumb_download']), file=code)
        print("fanart = " + str(json_config['fanart_download']), file=code)
        print("extrafanart = " + str(json_config['extrafanart_download']), file=code)
        print("extrafanart_copy = " + str(json_config['extrafanart_copy']), file=code)
        print("nfo = " + str(json_config['nfo_download']), file=code)
    code.close()


def check_pic(path_pic):
    if os.path.exists(path_pic):
        try:
            img = Image.open(path_pic)
            img.load()
            return True
        except:
            try:
                os.removie(path_pic)
            except:
                pass
            # print('文件损坏')
    return False

