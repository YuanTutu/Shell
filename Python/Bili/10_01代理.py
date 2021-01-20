# -*- coding:utf-8 -*-
#主要是一种反-反爬机制的方法，主要针对封印IP
#什么是代理：代理服务器
#突破自身IP访问限制
#隐藏自身真实IP
#代理相关网站  快代理  西祠代理  www.goubanjia.com
#代理ip的类型分http和https两种，只能一一对应的应用
#代理IP的匿名度
# 透明：服务器知道该次请求使用了代理，也知道请求对应的真实IP
# 匿名：知道使用了代理但不知道真实IP
# 高匿：不知道使用了代理，也不知道真实IP
import requests
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}

page_text = requests.get(url=url,headers=headers,proxies={"https":"36.25.30.233:9999"}).text

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

#反爬机制：封IP
#反反爬机制：使用代理