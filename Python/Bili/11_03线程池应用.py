# -*- coding=utf-8 -*-
import requests
from lxml import etree
#需求：爬取梨视频的视频数据
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}
#原则：线程池处理的是阻塞且耗时的部分

#对下述url发起请求解析出视频详情url和视频名称
url = 'https://www.pearvideo.com/category_5'
page_text= requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list=tree.xpath('//ul[@id="listvideoListUl"]/li')
for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    print(detail_url,name)
    #对详情页url发起请求
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    #从详情页中解析出视频的url
    


