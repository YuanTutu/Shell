# --coding:utf-8--
import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_search_web():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    for i in range(50):
        #print(i)
        url = 'https://www.baidu.com/s?wd=2018%E5%B9%B4%20%E5%A4%A7%E5%AD%A6%E7%94%9F%20intitle%3A%E8%87%AA%E6%9D%80' + '&pn=' + str(i * 10)
        response = requests.get(url=url, headers=header)
        result = response.text
        soup = BeautifulSoup(result, 'html.parser')
        h3 = soup.find_all('h3')
        for i in h3:
            a = i.a
            try:
                href = a.attrs['href']
                #print(href)
                b = a.text
                #print(b)
                with open('search.txt', 'a', encoding='utf-8') as f:
                    f.write(b+'\n'+href+'\n\n')
                    f.close()
            except:
                print('Error')


if __name__ == '__main__':
    get_search_web()