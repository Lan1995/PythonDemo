# -*- coding:utf-8 -*-
__author__ = 'LQ'
import requests
import bs4
from bs4 import BeautifulSoup

global headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

global server
server = 'http://www.biquge.cm'

global path
path = 'G:/星辰变'

global total_page
total_page = 'http://www.biquge.cm/2/2042/'


def getSoup(url):
    res = requests.get(url, headers=headers)
    # 1.获得总章数
    res.raise_for_status()
    # 2.格式化
    page_html = str(res.content, encoding='gbk')
    soup = BeautifulSoup(page_html, 'html.parser')
    return soup


if __name__ == '__main__':
    # 2.遍历获得每一页放入txt中

    soup = getSoup(total_page)
    pages = soup.find('div', id='list').findAll('a')
    print(type(pages))
    print('总章数：%d' % len(pages))

    count = 0
    for page in pages:
        count = count + 1
        print(type(page))
        end_url = page.get('href')
        content_soup = getSoup(server + end_url)
        content = content_soup.findAll('div', id='content')
        content = content[0].text.replace('\xa0' * 4, '\n')
        with open(path + "\\" + page.text.replace('?', '') + ".txt", 'w') as f:
            f.write(content)
