#--coding:utf-8--
import requests
from lxml import etree
import os
import time
from bs4 import BeautifulSoup

def get_search_web():
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    for i in range(2):
        print(i)
        url = 'https://www.baidu.com/s?wd=%E5%A4%A7%E5%AD%A6%E7%94%9F%E8%87%AA%E6%9D%80' + '&pn=' + str(i * 10)
        response = requests.get(url=url, headers=header)
        result = response.text
        #print(result)
        with open('{}.html'.format(i), 'a', encoding='utf-8') as f:
            f.write(result)
            f.close()
        
        soup = BeautifulSoup(result, 'html.parser') 
        h3 = soup.find_all('h3')
        #print(h3)
        for i in h3:
            #print(i)
            a = i.a
            try:
                href = a.attrs['href']
                b=a.text
                with open('search.txt', 'a', encoding='utf-8') as f:
                    f.write(b)
                    f.close()
                #获取a标签中的文字
                print(a.text, '\n', href)


            except:
                print('Error2')


            
# #对html进行解析
# def processing_html():
#     for i in range(2):
#         f = open('{}.html'.format(i),'r', encoding='utf-8')
#         content = f.read()
#         f.close()
#         html = etree.HTML(content)
#         #//*[@id="1"]/h3/a/text()[1]
#         #//*[@id="3"]/h3/a/text()[1]
#         result1 = html.xpath('//*[@id="1"]/h3')
#         print(result1)
#         #return result
#         #//*[@id="1"]/h3/a/em
#         result2 = html.xpath('//*[@id="1"]/h3/a/em')
#         #print(result2)
#         #//*[@id="1"]/h3/a/text()[2]
#         result3 = html.xpath('//*[@id="1"]/h3/a/text()[2]')
#         #print(result3)

def save(b,href):
    with open('search.txt', 'w', encoding='utf-8') as f:
        f.write(b)
        f.close()





if __name__ == '__main__':
    b,href=get_search_web()
    #processing_html()
    save(b,href)