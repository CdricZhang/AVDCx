import time
import os
from configparser import RawConfigParser

# ====================================================================================================================返回config_global

config_global = {}


def get_config() -> dict:
    global config_global
    if not config_global:
        print('读取config.ini，生成config_global！')
        read_config()
    return config_global


# ====================================================================================================================读取config.ini


def read_config() -> dict:
    config_file = 'config.ini'
    if not os.path.exists(config_file):
        config_file = '../config.ini'
        if not os.path.exists(config_file):
            print('config.ini未找到！')
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    json_config = {
        'main_mode': config.getint('common', 'main_mode'),
        'no_nfo_scrape': config.get('common', 'no_nfo_scrape'),
        'main_like': config.getint('common', 'main_like'),
        'more_website': config.get('common', 'more_website'),
        'success_file_move': config.getint('common', 'success_file_move'),
        'failed_file_move': config.getint('common', 'failed_file_move'),
        'success_file_rename': config.getint('common', 'success_file_rename'),
        'del_empty_folder': config.getint('common', 'del_empty_folder'),
        'soft_link': config.getint('common', 'soft_link'),
        'show_poster': config.getint('common', 'show_poster'),
        'translate_language': config.get('common', 'translate_language'),
        'translate_content': config.get('common', 'translate_content'),
        'translate_by': config.get('common', 'translate_by'),
        'deepl_key': config.get('common', 'deepl_key'),
        'actor_output': config.get('common', 'actor_output'),
        'info_output': config.get('common', 'info_output'),
        'website': config.get('common', 'website'),
        'series_as_set': config.getint('common', 'series_as_set'),
        'type': config.get('proxy', 'type'),
        'proxy': config.get('proxy', 'proxy'),
        'timeout': config.getint('proxy', 'timeout'),
        'retry': config.getint('proxy', 'retry'),
        'javbus_website': config.get('proxy', 'javbus_website'),
        'javdb_website': config.get('proxy', 'javdb_website'),
        'javdb': config.get('Cookies', 'javdb'),
        'folder_name': config.get('Name_Rule', 'folder_name'),
        'naming_file': config.get('Name_Rule', 'naming_file'),
        'naming_media': config.get('Name_Rule', 'naming_media'),
        'folder_name_max': config.getint('Name_Rule', 'folder_name_max'),
        'file_name_max': config.getint('Name_Rule', 'folder_name_max'),
        'actor_name_max': config.getint('Name_Rule', 'actor_name_max'),
        'actor_name_more': config.get('Name_Rule', 'actor_name_more'),
        'actor_no_name': config.get('Name_Rule', 'actor_no_name'),
        'pic_name': config.getint('Name_Rule', 'pic_name'),
        'cd_name': config.getint('Name_Rule', 'cd_name'),
        'cnword_char': config.get('Name_Rule', 'cnword_char'),
        'cnword_style': config.get('Name_Rule', 'cnword_style'),
        'folder_cnword': config.getint('Name_Rule', 'folder_cnword'),
        'file_cnword': config.getint('Name_Rule', 'file_cnword'),
        'del_actor_name': config.getint('Name_Rule', 'del_actor_name'),
        'media_path': config.get('media', 'media_path'),
        'success_output_folder': config.get('media', 'success_output_folder'),
        'failed_output_folder': config.get('media', 'failed_output_folder'),
        'extrafanart_folder': config.get('media', 'extrafanart_folder'),
        'media_type': config.get('media', 'media_type'),
        'sub_type': config.get('media', 'sub_type'),
        'folders': config.get('escape', 'folders'),
        'string': config.get('escape', 'string'),
        'file_size': config.getfloat('escape', 'file_size'),
        'emby_url': config.get('emby', 'emby_url'),
        'api_key': config.get('emby', 'api_key'),
        'actor_photo_folder': config.get('emby', 'actor_photo_folder'),
        'actor_photo_upload': config.get('emby', 'actor_photo_upload'),
        'poster_mark': config.getint('mark', 'poster_mark'),
        'thumb_mark': config.getint('mark', 'thumb_mark'),
        'mark_size': config.getint('mark', 'mark_size'),
        'mark_type': config.get('mark', 'mark_type'),
        'mark_pos': config.get('mark', 'mark_pos'),
        'download_nfo': config.get('file_download', 'download_nfo'),
        'download_poster': config.get('file_download', 'download_poster'),
        'download_thumb': config.get('file_download', 'download_thumb'),
        'download_fanart': config.get('file_download', 'download_fanart'),
        'download_extrafanart': config.get('file_download', 'download_extrafanart'),
        'download_extrafanart_copy': config.get('file_download', 'download_extrafanart_copy'),
        'keep_local_nfo': config.get('file_download', 'keep_local_nfo'),
        'keep_local_poster': config.get('file_download', 'keep_local_poster'),
        'keep_local_thumb': config.get('file_download', 'keep_local_thumb'),
        'keep_local_fanart': config.get('file_download', 'keep_local_fanart'),
        'keep_local_extrafanart': config.get('file_download', 'keep_local_extrafanart'),
        'keep_local_extrafanart_copy': config.get('file_download', 'keep_local_extrafanart_copy'),
        'poster_from': config.get('file_download', 'poster_from'),
        'update_check': config.getint('update', 'update_check'),
        'switch_debug': config.getint('debug_mode', 'switch'),
        'save_log': config.getint('log', 'save_log'),
    }
    print('config.ini read done!')
    update_config(json_config)                                                 # 更新config_global


# ====================================================================================================================更新config_global


def update_config(json_config) -> dict:
    global config_global

    # 获取proxies
    if json_config['type'] == 'http':
        json_config['proxies'] = {"http": "http://" + json_config['proxy'], "https": "http://" + json_config['proxy']}
    elif json_config['type'] == 'socks5':
        json_config['proxies'] = {"http": "socks5h://" + json_config['proxy'], "https": "socks5h://" + json_config['proxy']}
    else:
        json_config['proxies'] = None

    # 获取javdb_cookie
    cookies_value = json_config['javdb']
    if cookies_value:
        json_config['javdb_cookie'] = {'cookie': cookies_value}
    else:
        json_config['javdb_cookie'] = None

    # 获取网址
    json_config['javbus_website'] = json_config['javbus_website'].replace('https://', '').replace('http://', '').strip('/')
    json_config['javdb_website'] = json_config['javdb_website'].replace('https://', '').replace('http://', '').strip('/')

    config_global = json_config
    print('config.ini update done!')


# ====================================================================================================================恢复默认配置


def init_config():
    json_config = {
        'main_mode': 1,
        'no_nfo_scrape': 'off',
        'main_like': 1,
        'more_website': 'javdb,jav321,javlibrary',
        'success_file_move': 1,
        'failed_file_move': 1,
        'success_file_rename': 1,
        'del_empty_folder': 1,
        'soft_link': 0,
        'show_poster': 1,
        'translate_language': 'zh_cn',
        'translate_content': 'title,outline',
        'translate_by': 'youdao',
        'deepl_key': '',
        'actor_output': 'zh_cn',
        'info_output': 'zh_cn',
        'website': 'all',
        'series_as_set': 1,
        'type': 'no',
        'proxy': '127.0.0.1:7890',
        'timeout': 10,
        'retry': 3,
        'javbus_website': '',
        'javdb_website': '',
        'javdb': '',
        'folder_name': 'actor/number actor',
        'naming_file': 'number',
        'naming_media': 'number title',
        'folder_name_max': 70,
        'file_name_max': 70,
        'actor_name_max': 3,
        'actor_name_more': '等演员',
        'actor_no_name': '未知演员',
        'pic_name': 0,
        'cd_name': 0,
        'cnword_char': '-C.,中文,字幕',
        'cnword_style': '-C',
        'folder_cnword': 1,
        'file_cnword': 1,
        'del_actor_name': 1,
        'media_path': '',
        'success_output_folder': 'JAV_output',
        'failed_output_folder': 'failed',
        'extrafanart_folder': '',
        'media_type': '.mp4|.avi|.rmvb|.wmv|.mov|.mkv|.flv|.ts|.webm|.iso|.mpg',
        'sub_type': '.smi|.srt|.idx|.sub|.sup|.psb|.ssa|.ass|.txt|.usf|.xss|.ssf|.rt|.lrc|.sbv|.vtt|.ttml',
        'folders': 'JAV_output,examples',
        'string': '1080p,720p,22-sht.me,-HD,bbs2048.org@,hhd800.com@,icao.me@,hhb_000',
        'file_size': '100.0',
        'emby_url': 'http://192.168.5.191:8096',
        'api_key': 'cb83900340b447fab785cb628a99c3da',
        'actor_photo_folder': '',
        'actor_photo_upload': 'on',
        'poster_mark': 1,
        'thumb_mark': 1,
        'mark_size': 5,
        'mark_type': 'SUB,LEAK,UNCENSORED',
        'mark_pos': 'top_left',
        'download_nfo': 'on',
        'download_poster': 'on',
        'download_thumb': 'on',
        'download_fanart': 'on',
        'download_extrafanart': 'off',
        'download_extrafanart_copy': 'off',
        'keep_local_nfo': 'off',
        'keep_local_poster': 'off',
        'keep_local_fanart': 'off',
        'keep_local_thumb': 'off',
        'keep_local_extrafanart': 'off',
        'keep_local_extrafanart_copy': 'off',
        'poster_from': 'auto',
        'update_check': 1,
        'switch_debug': 1,
        'save_log': 1,
    }
    print('config.ini restore done!')
    save_config(json_config)


# ====================================================================================================================保存配置到config.ini


def save_config(json_config):
    config_file = 'config.ini'
    with open(config_file, "wt", encoding='UTF-8') as code:
        print("[modified_time]", file=code)
        print("modified_time = " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), file=code)
        print("", file=code)
        print("[common]", file=code)
        print("main_mode = " + str(json_config['main_mode']), file=code)
        print("no_nfo_scrape = " + str(json_config['no_nfo_scrape']), file=code)
        print("main_like = " + str(json_config['main_like']), file=code)
        print("more_website = " + str(json_config['more_website']), file=code)
        print("success_file_move = " + str(json_config['success_file_move']), file=code)
        print("failed_file_move = " + str(json_config['failed_file_move']), file=code)
        print("success_file_rename = " + str(json_config['success_file_rename']), file=code)
        print("del_empty_folder = " + str(json_config['del_empty_folder']), file=code)
        print("soft_link = " + str(json_config['soft_link']), file=code)
        print("show_poster = " + str(json_config['show_poster']), file=code)
        print("translate_language = " + str(json_config['translate_language']), file=code)
        print("translate_content = " + str(json_config['translate_content']), file=code)
        print("translate_by = " + str(json_config['translate_by']), file=code)
        print("deepl_key = " + str(json_config['deepl_key']), file=code)
        print("actor_output = " + str(json_config['actor_output']), file=code)
        print("info_output = " + str(json_config['info_output']), file=code)
        print("website = " + str(json_config['website']), file=code)
        print("series_as_set = " + str(json_config['series_as_set']), file=code)
        print("# translate_language: zh_cn, zh_tw, ja", file=code)
        print("# translate_by: youdao, deepl", file=code)
        print("# actor_output: zh_cn, zh_tw, ja, no", file=code)
        print("# info_output: zh_cn, zh_tw, ja, no", file=code)
        print("# website: all, iqqtv, javbus, javdb, jav321, dmm, avsox, xcity, mgstage, fc2, fc2club, fc2hub, airav, javlibrary", file=code)
        print("", file=code)
        print("[proxy]", file=code)
        print("type = " + json_config['type'], file=code)
        print("proxy = " + str(json_config['proxy']), file=code)
        print("timeout = " + str(json_config['timeout']), file=code)
        print("retry = " + str(json_config['retry']), file=code)
        print("javbus_website = " + str(json_config['javbus_website']), file=code)
        print("javdb_website = " + str(json_config['javdb_website']), file=code)
        print("# type: no, http, socks5", file=code)
        print("", file=code)
        print("[Cookies]", file=code)
        print("javdb = " + str(json_config['javdb']), file=code)
        print("# cookies存在有效期，记得更新", file=code)
        print("", file=code)
        print("[Name_Rule]", file=code)
        print("folder_name = " + str(json_config['folder_name']), file=code)
        print("naming_file = " + str(json_config['naming_file']), file=code)
        print("naming_media = " + str(json_config['naming_media']), file=code)
        print("folder_name_max = " + str(json_config['folder_name_max']), file=code)
        print("file_name_max = " + str(json_config['file_name_max']), file=code)
        print("actor_name_max = " + str(json_config['actor_name_max']), file=code)
        print("actor_name_more = " + str(json_config['actor_name_more']), file=code)
        print("actor_no_name = " + str(json_config['actor_no_name']), file=code)
        print("pic_name = " + str(json_config['pic_name']), file=code)
        print("cd_name = " + str(json_config['cd_name']), file=code)
        print("cnword_char = " + str(json_config['cnword_char']), file=code)
        print("cnword_style = " + str(json_config['cnword_style']), file=code)
        print("folder_cnword = " + str(json_config['folder_cnword']), file=code)
        print("file_cnword = " + str(json_config['file_cnword']), file=code)
        print("del_actor_name = " + str(json_config['del_actor_name']), file=code)
        print("# 命名字段有：title, actor, number, studio, publisher, year, mosaic, runtime, director, release, series, definition, cnword", file=code)
        print("", file=code)
        print("[media]", file=code)
        print("media_path = " + str(json_config['media_path']), file=code)
        print("success_output_folder = " + str(json_config['success_output_folder']), file=code)
        print("failed_output_folder = " + str(json_config['failed_output_folder']), file=code)
        print("extrafanart_folder = " + str(json_config['extrafanart_folder']), file=code)
        print("media_type = " + str(json_config['media_type']), file=code)
        print("sub_type = " + str(json_config['sub_type']), file=code)
        print("", file=code)
        print("[escape]", file=code)
        print("folders = " + str(json_config['folders']), file=code)
        print("string = " + str(json_config['string']), file=code)
        print("file_size = " + str(json_config['file_size']), file=code)
        print("", file=code)
        print("[emby]", file=code)
        print("emby_url = " + str(json_config['emby_url']), file=code)
        print("api_key = " + str(json_config['api_key']), file=code)
        print("actor_photo_folder = " + str(json_config['actor_photo_folder']), file=code)
        print("actor_photo_upload = " + str(json_config['actor_photo_upload']), file=code)
        print("", file=code)
        print("[mark]", file=code)
        print("poster_mark = " + str(json_config['poster_mark']), file=code)
        print("thumb_mark = " + str(json_config['thumb_mark']), file=code)
        print("mark_size = " + str(json_config['mark_size']), file=code)
        print("mark_type = " + str(json_config['mark_type']), file=code)
        print("mark_pos = " + str(json_config['mark_pos']), file=code)
        print("# mark_size: range 1-5", file=code)
        print("# mark_type: sub, leak, uncensored", file=code)
        print("# mark_pos: bottom_right, bottom_left, top_right, top_left", file=code)
        print("", file=code)
        print("[file_download]", file=code)
        print("download_nfo = " + str(json_config['download_nfo']), file=code)
        print("download_poster = " + str(json_config['download_poster']), file=code)
        print("download_thumb = " + str(json_config['download_thumb']), file=code)
        print("download_fanart = " + str(json_config['download_fanart']), file=code)
        print("download_extrafanart = " + str(json_config['download_extrafanart']), file=code)
        print("download_extrafanart_copy = " + str(json_config['download_extrafanart_copy']), file=code)
        print("keep_local_nfo = " + str(json_config['keep_local_nfo']), file=code)
        print("keep_local_poster = " + str(json_config['keep_local_poster']), file=code)
        print("keep_local_thumb = " + str(json_config['keep_local_thumb']), file=code)
        print("keep_local_fanart = " + str(json_config['keep_local_fanart']), file=code)
        print("keep_local_extrafanart = " + str(json_config['keep_local_extrafanart']), file=code)
        print("keep_local_extrafanart_copy = " + str(json_config['keep_local_extrafanart_copy']), file=code)
        print("poster_from = " + str(json_config['poster_from']), file=code)
        print("# poster_from: auto, download", file=code)
        print("", file=code)
        print("[update]", file=code)
        print("update_check = " + str(json_config['update_check']), file=code)
        print("", file=code)
        print("[debug_mode]", file=code)
        print("switch = " + str(json_config['switch_debug']), file=code)
        print("", file=code)
        print("[log]", file=code)
        print("save_log = " + str(json_config['save_log']), file=code)

    code.close()
    print('config.ini save done!')
    update_config(json_config)                                                 # 更新config_global
