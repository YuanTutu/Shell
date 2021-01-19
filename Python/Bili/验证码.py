# -*- coding=utf-8 -*-
import requests
from lxml import etree
from chaojiying import Chaojiying_Client
# if __name__ == '__main__':
#封装识别验证码图片的函数
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/84.0.4147.135Safari/537.36",
}

#将验证码图片下载到本地
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_img_src='https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src,headers=headers).content
#将验证码保存到本地
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
#调用chaojiying的东西
im = open('code.jpg', 'rb').read()
chaojiyinguser = Chaojiying_Client('yuanbo6', 'yuanbuo19941205', '643a35e1bf6b4f7a220c5c08989dd71e')
code_result = chaojiyinguser.PostPic(im,1902)#验证码结果
print(code_result)