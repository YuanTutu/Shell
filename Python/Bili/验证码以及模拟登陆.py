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
chaojiyinguser = Chaojiying_Client('超级鹰用户名', '超级鹰密码', '软件ID')
code_result = chaojiyinguser.PostPic(im,1902)#验证码结果
# print(type(code_result))
# print(code_result)
# print(code_result.get('pic_str'))
#获得的结果是一个字典，从字典中根据键提取值
yanzhengma=code_result.get('pic_str')
#尝试post发送数据模拟登陆
login_url='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'网站账号',
    'pwd':'网站密码',
    'code':yanzhengma,
    'denglu':'登录',
}
login_page_text=requests.post(url=login_url,headers=headers,data=data).text
response = requests.post(url=login_url,headers=headers,data=data)
print(response.status_code)
# print(type(login_page_text))
# 如果下面的模式还是wb而不是w则会因为str和byte的问题一直报错，参见https://blog.csdn.net/cathyspring/article/details/79444242
with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(login_page_text)

