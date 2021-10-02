import requests
import time
import random
import os
from lxml import etree
import json
import re

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}


def save_log(error_info):
    with open('_错误信息.txt', 'a', encoding='utf-8') as f:
        f.write(error_info)


def get_c_number():
    i = 1
    json_filename = 'c_number.json'
    if not os.path.exists(json_filename):
        with open(json_filename, 'w', encoding='utf-8') as f:
            f.write('{}')
    with open(json_filename, 'r', encoding='utf-8') as data:
        json_data = json.load(data)
    while i:
        url = ('https://www.sehuatang.org/forum-103-%s.html' % i)
        # 获取当前页面信息
        try:
            res = requests.get(url, headers=headers)
        except:
            print('获取当前页面信息失败！信息已保存到：_错误信息.txt')
            print(res.text)
            error_info = '\nPA 获取当前页面信息失败！\n' + url + '\n'
            i -= 1
        else:
            # 将html转成 Element对象，以便使用xpath定位
            html = etree.HTML(res.text.replace('encoding="utf-8"', ''))
            if i == 1:
                page_total = html.xpath('//a[@class="last"]/text()')[0][-3:]
                print('当前共 %s 页数据！' % page_total)
            print('\n' + '**' * 20)
            print('开始下载第 %s 页数据...\n页面地址：%s' % (i, url))
            # 获取当前页面帖子列表
            try:
                post_info = html.xpath('//tbody[contains(@id, "normal")]/tr/th/a[2]')
            except:
                print('获取当前页面帖子列表失败！信息已保存到：_错误信息.txt')
                error_info = '\nL 获取当前页面帖子列表失败！\n' + url + '\n'
                save_log(error_info)
            else:
                post_number = len(post_info)
                print('帖子数量：%s' % post_number)
                j = 0
                for each in post_info:
                    j += 1
                    post_title = each.text
                    # url_adress = each.attrib['href']
                    # 2021-06-01 發行日期: 2021-05-27 [大陆简化字][完美主义控][6000码率纯净版] NUKA-046 鶴川牧子
                    if 'KBPS' in post_title:
                        a = post_title[post_title.find('KBPS'):]
                        b = a[a.find(']') + 1:].strip()
                        number = b[:b.find(' ')]
                        title = b[b.find(' ') + 1:]
                    elif '6000' in post_title:
                        a = post_title[post_title.find('6000'):]
                        b = a[a.find(']') + 1:].strip()
                        number = b[:b.find(' ')]
                        title = b[b.find(' ') + 1:]
                    elif '3000' in post_title:
                        post_title1 = post_title.replace('[经典老片]', '')
                        a = post_title1[post_title1.find('3000'):]
                        b = a[a.find(']') + 1:].strip()
                        number = b[:b.find(' ')]
                        title = b[b.find(' ') + 1:]
                    elif '5500' in post_title:
                        post_title1 = post_title.replace('[经典老片]', '')
                        a = post_title1[post_title1.find('5500'):]
                        b = a[a.find(']') + 1:].strip()
                        number = b[:b.find(' ')]
                        title = b[b.find(' ') + 1:]
                    # missax.17.03.13.lana.rhoades.please.help.me-请帮帮我
                    elif re.search(r'\.\d{2}\.\d{2}\.\d{2}', post_title):
                        number = post_title[:post_title.find('-')]
                        title = post_title[post_title.find('-') + 1:]
                    # JUL-618 【第一次！】madonna初登场！【
                    elif re.findall(r'^[A-Za-z0-9-_ ]+', post_title):
                        number = re.findall(r'^[A-Za-z0-9-]+', post_title)[0]
                        title = post_title.replace(number, '').strip()
                    else:
                        number = post_title[:post_title.find(' ')]
                        title = post_title[post_title.find(' ') + 1:]
                    number = number.upper().replace(' - ', '').replace(' -', '').replace('- ', '').strip()
                    title = title.replace('[高清中文字幕]', '').replace('[高清中文字幕', '').replace('高清中文字幕]', '').replace('【高清中文字幕】', '').strip()
                    json_data[number] = title
                    print(j)
                    print(post_title)
                    print(number + ' : ' + title)
            print('\n当前第 %s 页数据...\n页面地址：%s' % (i, url))
            print('**' * 20)
            with open(json_filename, 'w', encoding='utf-8') as f:
                json.dump(
                    json_data,
                    f,
                    ensure_ascii=False,
                    sort_keys=True,
                    indent=4,
                    separators=(',', ':'),
                )
            if i < int(page_total):
                i += 1
            else:
                i = 0
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    print('.......')
    try:
        os.remove('_错误信息.txt')
    except:
        pass
    get_c_number()
    print('\n\n# ===== 处理完成！ ===== #\n')
