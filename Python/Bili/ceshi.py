import requests
import re
import threading
import json
#跟着B站测试爬取排行榜的内容   https://www.bilibili.com/video/BV1mK4y1E75Y/
#blog https://www.cnblogs.com/hhh188764/p/14183816.html

# 从详情页中解析出视频的url
# 视频链接存放的文件
# https://www.pearvideo.com/videoStatus.jsp?contId=1716852&mrd=0.2335615752414648
# 瀑布流链接
# https://www.pearvideo.com/popular_loading.jsp?reqType=1&categoryId=&start=20&sort=2&mrd=0.7711852368514107
# 假的视频连接
# https://video.pearvideo.com/mp4/third/20210118/1611151077092-15765543-133916-hd.mp4
# 真实视频链接
# https://video.pearvideo.com/mp4/third/20210118/cont-1716852-15765543-133916-hd.mp4
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
    #获取假的视频链接
    result = json.loads(response)
    F_v_url=result["videoInfo"]["videos"]["srcUrl"]
    # print("假视频url：",F_v_url)
    suffux=F_v_url.split('-')[1]
    # print("看起来是防伪内容：",suffux)
    jiewei=F_v_url.split('-')[2]
    # print(jiewei)
    date=F_v_url.split('/')[-2]
    # print("日期：",date)

    T_v_url = 'https://video.pearvideo.com/mp4/third/{}/cont-{}-{}-{}-hd.mp4'.format(date,video_id,suffux,jiewei)
    # print("组成结果:",T_v_url)
    # print("实际结果: https://video.pearvideo.com/mp4/third/20210118/cont-1716942-15690592-193344-hd.mp4")
    return  T_v_url

def save_video(video_url,titles):
    video_content = get_response(video_url).content
    filename = titles + '.mp4'
    with open(filename, mode='wb') as f:
        f.write(video_content)
        print('正在保存：',titles)
        print(video_url)

for page in range(0,10,10):#80为上限
    url = 'https://www.pearvideo.com/popular_loading.jsp'
    params = {
        'reqType':'1',
        'categoryId':'',
        'start':'{}'.format(page),
        'sort':'10',
        'mrd':'0.7711852368514107'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers,params=params)
    # print(response.text)

    titles = re.findall('<h2 class="popularem-title">(.*?)</h2>',response.text)
    num_id = re.findall('<a href="video_(\d+)" class="popularembd actplay">', response.text)
    # print(titles)
    # print(num_id)
    video_url=get_url(num_id[0])
