import requests
from lxml import etree
import os
import time

# 获取小说主页的hmtl
#目前只测试了这个biquge5200的网站，其他的网站还么测试
def get_main_html():
    url = 'https://www.biquge5200.com/75_75584/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    response = requests.get(url=url,headers=header)
    jianlai= response.text
    #这里会保存一个主页用于提取每一章节的链接
    with open('jianlai.html', 'a') as f:
        f.write(jianlai)
        f.close()

#对html进行解析，获取每一章节的链接
def processing_html():
    f = open('jianlai.html','r')
    content = f.read()
    f.close()
    html = etree.HTML(content)
    result = html.xpath('//*[@id="list"]/dl/dd/a/@href')
    print(result)
    return result

#把文章目录的链接保存成list文件
#如果要读取文件做列表，需要手动删除前面显示的九章链接
#需要注意把每一个链接进行换行操作
def make_list(result):
    article = str(result)
    with open('jianlai.list', 'w') as f:
        f.write(article)
        f.close()

#把list文件内容转换成列表，方便读取
def file_to_list():
    f = open(r'jianlai.list','r')
    urls = list(f)
    #print(urls)
    f.close()
    return urls

#开始访问每一章节并保存成html
#需要注意在当前爬虫所在路径下创建一个JIANLAI文件夹，JIANLAI就是剑来，你可以换成其他小说名，上面的list名字也是一样
def open_everyone(urls):
    for url in urls:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        try:
            response = requests.get(url,headers=header)
            date = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
            with open('JIANLAI/' + format(date) + '.html', 'w') as f:
                f.write(response.text)
                f.close()
            time.sleep(3)#别太嚣张，每隔三秒访问一章，免得被人家给禁了（盗版小说网站应该没这个本事吧）
        except:
            print(url+"is error")#如果有哪一章节报错就打印出来，方便回头单独处理。当然其实可以改成保存出一个文件的形式

#开始解析html内容,并保存成txt
def get_articles():
    path = "D:/00workspace/99tools/JIANLAI/"
    files = os.listdir(path)
    for file in files:
        f = open(path+file,'r')
        content = f.read()
        f.close()
        html = etree.HTML(content)
        try:
            result = html.xpath('//*[@id="content"]/p/text()')
            article = str(result)
            with open('TXT/jianlai.txt', 'a') as f:#小说名可以替换
                f.write('\t' + article + '\r\n')
                f.close()
        except:
            pass


#习惯挨个执行，执行完了就注释掉，比较稳
#后三个函数倒是可以放一起执行
def main():
    #get_main_html()
    #result=processing_html()
    #make_list(result)
    urls=file_to_list()
    open_everyone(urls)
    get_articles()

if __name__ == '__main__':
    main()