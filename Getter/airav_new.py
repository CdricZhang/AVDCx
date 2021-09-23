import json
from Getter import airav
from configparser import RawConfigParser

def getDelActorName():
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    del_actor_name = config.getint('Name_Rule', 'del_actor_name')
    return del_actor_name

def getDataState(json_data):
    if json_data['title'] == '' or json_data['title'] == 'None' or json_data['title'] == 'null':
        return False
    else:
        return True


def main(number, appoint_url='', translate_language='zh_cn', log_info='', req_web='', isuncensored=False):
    config_file = 'config.ini'
    config = RawConfigParser()
    config.read(config_file, encoding='UTF-8')
    translate_language = config.get('common', 'translate_language')
    translate_content = config.get('common', 'translate_content')
    actor_output = config.get('common', 'actor_output')
    info_output = config.get('common', 'info_output')

    if 'cn.airav.wiki' in appoint_url:
        appoint_url = appoint_url.replace('cn.airav.wiki', 'jp.airav.wiki').replace('?lng=zh-CN', '') + '?lng=jp'
    elif 'www.airav.wiki' in appoint_url:
        appoint_url = appoint_url.replace('www.airav.wiki', 'jp.airav.wiki').replace('?lng=zh-TW', '') + '?lng=jp'
    elif 'jp.airav.wiki' in appoint_url:
        appoint_url = appoint_url.replace('?lng=jp', '') + '?lng=jp'
    json_data = json.loads(airav.main(number, appoint_url, translate_language='jp'))
    if not getDataState(json_data):
        return json.dumps(json_data, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'), )
    if translate_language != 'ja':
        if translate_language == 'zh_cn':
            appoint_url = json_data['website'].replace('jp.airav.wiki', 'cn.airav.wiki').replace('?lng=jp', '?lng=zh-CN')
        else:
            appoint_url = json_data['website'].replace('jp.airav.wiki', 'www.airav.wiki').replace('?lng=jp', '?lng=zh-TW')
        log_info = json_data['log_info']
        req_web = json_data['req_web']
        json_data_zh = json.loads(airav.main(number, appoint_url, translate_language, log_info, req_web))
        if getDataState(json_data_zh):
            json_data['req_web'] = json_data_zh['req_web']
            json_data['website'] = json_data_zh['website']
            if 'title' in translate_content:
                json_data['title'] = json_data_zh['title']
                if getDelActorName():
                    json_data['title'] = json_data['title'].replace(' ' + json_data['actor'], '').strip(' ')
            if 'outline' in translate_content:
                json_data['outline'] = json_data_zh['outline']
            if actor_output != 'ja':
                json_data['actor'] = json_data_zh['actor']
            if info_output != 'ja':
                json_data['tag'] = json_data_zh['tag']

    js = json.dumps(json_data, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
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
