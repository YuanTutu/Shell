from selenium import webdriver
import time
from PIL import Image
from chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--window-size=1920,1080')
# bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options)
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.maximize_window()

bro.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)

a_tag = bro.find_element_by_class_name('login-hd-account')
a_tag.click()
time.sleep(1)
# save_screenshot将当前页面进行截图
bro.save_screenshot('./aaa.png')
#确定验证码图片左上角右下角坐标，做裁剪区域
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img_ele.location#验证码左上角坐标x,y
print(location)
size = code_img_ele.size#验证码标签对应的长和宽
print(size)
#左上角和右下角坐标
# rangle = (
# int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])
# )
# print(rangle)
#至此验证码图片区域就确定下来了
rangle = (1600,370,1980,590)#2K分辨率的屏幕是需要单独查找位置的，无法直接用视频里面的操作计算，会产生偏差

i = Image.open('./aaa.png')
code_img_name = './code.png'
#crop根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)


im = open('code.png', 'rb').read()
chaojiyinguser = Chaojiying_Client('超级鹰账号', '超级鹰密码', '超级鹰ID')
code_result = chaojiyinguser.PostPic(im,9004)#code_result是json所以下面要get
result=code_result.get('pic_str')
print(result)
all_list=[]#存储即将被点击的点的坐标[[x1,y1],[x2,y2]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])-30
        y = int(list_1[i].split(',')[1])-20
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])-30
    y = int(result.split(',')[1])-20
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
# print(all_list)
#遍历列表，使用动作链对每一个列表元素对应的xy坐标进行点击
for l in all_list:
    print(l)
    x=l[0]
    y=l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele,x,y).click().perform()
    time.sleep(0.5)

bro.find_element_by_id('J-userName').send_keys('12306账号')
time.sleep(0.5)
bro.find_element_by_id('J-password').send_keys('12306密码')
time.sleep(0.5)
bro.find_element_by_id('J-login').click()
time.sleep(5)
bro.quit()