from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.taobao.com')

#标签定位
search_input = bro.find_element_by_id('q')
#标签交互
search_input.send_keys('Iphone')

#执行一组js
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(5)

#点击搜素按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

bro.get('https://www.baidu.com')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()

sleep(5)

bro.quit()