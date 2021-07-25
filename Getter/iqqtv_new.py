import json
from Getter import javdb, iqqtv, jav321
from configparser import RawConfigParser
import time

def getDataState(json_data):
    if json_data['title'] == '' or json_data['title'] == 'None' or json_data['title'] == 'null':
        return False
    else:
        return True

def getMode():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    translate_language = config.get('common', 'translate_language')
    translate_content = config.get('common', 'translate_content')
    main_like = config.getint('common', 'main_like')    # 当偏好速度时，只需要请求一次页面，这个决定要不要请求javdb
    return translate_language, translate_content, main_like

def main(number, appoint_url='', translate_language='zh_cn', log_info='', req_web='', isuncensored=False):
    translate_language, translate_content, main_like = getMode()
    json_data = json.loads(iqqtv.main(number, appoint_url, translate_language='jp'))
    if not getDataState(json_data):
        return json_data
    if translate_language != 'ja':
        if translate_language == 'zh_cn':
            appoint_url = json_data['website'].replace('/jp/', '/cn/')
        else:
            appoint_url = json_data['website'].replace('/jp/', '/')
        log_info = json_data['log_info']
        req_web = json_data['req_web']
        # time.sleep(0.5)
        json_data_zh = json.loads(iqqtv.main(number, appoint_url, translate_language, log_info, req_web))
        if getDataState(json_data_zh):
            json_data['req_web'] = json_data_zh['req_web']
            json_data['website'] = json_data_zh['website']
            if 'title' in translate_content:
                json_data['title'] = json_data_zh['title']
            if 'outline' in translate_content:
                json_data['outline'] = json_data_zh['outline']
            if 'actor' in translate_content:
                json_data['actor'] = json_data_zh['actor']
            if 'tag' in translate_content:
                json_data['tag'] = json_data_zh['tag']
    if main_like:
        req_web = json_data['req_web']
        json_data_jav321 = json.loads(jav321.main(number, '', log_info, req_web))
        if getDataState(json_data_jav321):
            json_data['req_web'] = json_data_jav321['req_web']
            json_data['runtime'] = json_data_jav321['runtime']
            json_data['score'] = json_data_jav321['score']
            json_data['series'] = json_data_jav321['series']
            json_data['director'] = json_data_jav321['director']
            json_data['extrafanart'] = json_data_jav321['extrafanart']
    return json_data


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
