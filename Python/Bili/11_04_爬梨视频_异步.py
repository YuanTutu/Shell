import requests
import re
import threading
import json
from multiprocessing.dummy import Pool
import time
#跟着B站测试爬取排行榜的内容   https://www.bilibili.com/video/BV1mK4y1E75Y/
#blog https://www.cnblogs.com/hhh188764/p/14183816.html

def change_title(title):
    pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|\：\《\》\,\，\!\！\?\？\、]")  # '/ \ : * ? " < > |'
    new_title = re.sub(pattern, "_", title)  # 替换为下划线
    return new_title


def get_response(html_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    response = requests.get(url=html_url, headers=headers)
    return response

def get_url(video_id):
    url = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd=0.2335615752414648'.format(video_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Referer':'https://www.pearvideo.com/video_{}'.format(video_id)#防盗链
    }
    response=requests.get(url=url,headers=headers).text
    result = json.loads(response)
    F_v_url=result["videoInfo"]["videos"]["srcUrl"]
    suffux=F_v_url.split('-')[1]
    jiewei=F_v_url.split('-')[2]
    date=F_v_url.split('/')[-2]

    T_v_url = 'https://video.pearvideo.com/mp4/third/{}/cont-{}-{}-{}-hd.mp4'.format(date,video_id,suffux,jiewei)
    # print("组成结果:",T_v_url)
    return  T_v_url


def save_video(video_url,titles):
    video_content = get_response(video_url).content
    # filename = titles[0] + '.mp4'
    filename = titles + '.mp4'
    print(filename)
    with open(filename, mode='wb') as f:
        f.write(video_content)
        print('正在保存：',titles)
        print(video_url+titles+'保存完成')

def get_video_data(dic):
    url = dic['url']
    print(dic['name']+'正在保存')

    data = requests.get(url=url,headers=headers).content
    #持久化存储
    with open(dic['name']+'.mp4','wb') as f:
        f.write(data)
        print(dic['name']+'保存完成')

urls=[]
for page in range(0,80,10):#80为上限
    url = 'https://www.pearvideo.com/popular_loading.jsp'
    params = {
        'reqType':'1',
        'categoryId':'',
        'start':'{}'.format(page),
        'sort':'10',
        'mrd':'0.7711852368514107',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    response=requests.get(url=url,headers=headers,params=params)
    titles = re.findall('<h2 class="popularem-title">(.*?)</h2>',response.text)
    num_id = re.findall('<a href="video_(\d+)" class="popularembd actplay">', response.text)
    for i in range(len(num_id)):
        video_url=get_url(num_id[i])
        new_title=change_title(titles[i])
        dic = {
            'name':new_title,
            'url':video_url,
        }
        urls.append(dic)
        # save_video(video_url,new_title)
pool = Pool(4)
start_time= time.time()
pool.map(get_video_data,urls)
end_time=time.time()
print('%d second'%(end_time-start_time))
pool.close()
pool.join()