from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')

a_tag=bro.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('944947973')
sleep(1)
password_tag.send_keys('Hik@123++')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()
#此处无法绕过滑动验证码
sleep(3)
bro.quit()