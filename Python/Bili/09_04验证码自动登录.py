# -*- coding=utf-8 -*-
# 参考自https://blog.csdn.net/qq_31910669/article/details/111590885
# 使用session没有问题，问题在于使用session的顺序
# 吐了
# 心态小崩
import requests
from lxml import etree
from chaojiying import Chaojiying_Client

def get_code():
    im = open('code.jpg', 'rb').read()
    chaojiyinguser = Chaojiying_Client('yuanbo6', 'yuanbuo19941205', '643a35e1bf6b4f7a220c5c08989dd71e')
    code_result = chaojiyinguser.PostPic(im,1902)
    yanzhengma=code_result.get('pic_str')
    return yanzhengma


url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}

session = requests.Session()

page_text = session.get(url=url,headers=headers).text
tree = etree.HTML(page_text)

code_img_src='https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = session.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)

__VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
code_text=get_code()
print(code_text)

data = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'944947973@qq.com',
    'pwd':'yuanbuo19941205',
    'code':code_text,
    'denglu':'登录',
}

login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
response = session.post(url=login_url,headers=headers,data=data)
print(response.status_code)
login_page_text=response.text

with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(login_page_text)