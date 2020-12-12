#--coding:utf-8--
#把汉字和你想要的的URL组合编码，行程网页编码
from urllib.parse import urlencode

start_url='http://tieba.baidu.com/f?'
urldata = {
    'kw':'诗人李白',
    'ie':'utf-8',
    'pn':'100',
}

print(start_url+urlencode(urldata))