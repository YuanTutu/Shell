# 高性能异步爬虫
# 目的，在爬虫中使用异步数据实现高性能的数据爬取操作
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}

urls={
    'https://www.job592.com/view/doc_downSuccess.show?id=1844&uid=a349ea5549f9f78f862e92d6043a6960&time=1611114238',
    'https://www.job592.com/view/doc_downSuccess.show?id=4216&uid=6bd0129fb9a538addefd0fb40f6e88d3&time=1611114278',
    'https://www.job592.com/view/doc_downSuccess.show?id=6228&uid=370743e69fd2c7abc447677177a4334a&time=1611114303'
}

def get_content(url):
    print('正在爬取：',url)
    #get方法其实是一个阻塞方法，当阻塞方法执行成功之后才会继续执行
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200 :
        return response.content

def parse_content(content):
    print('响应数据的长度为： ',len(content))

for url in urls:
    content = get_content(url)
    parse_content(content)
