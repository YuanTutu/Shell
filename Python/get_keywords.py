#--coding:utf-8--
import requests

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