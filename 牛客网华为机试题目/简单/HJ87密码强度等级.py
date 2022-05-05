import re

passwd=input()
core = 0

#密码长度
if len(passwd) <= 4:
    core = core + 5
elif 5 <= len(passwd) <= 7:
    core = core + 10
else:
    core = core + 25

#字母
Dxie = re.findall(r'[A-Z]',passwd)
Xxie = re.findall(r'[a-z]',passwd)
if bool(Dxie) == 1 and bool(Xxie) == 1:
    core = core + 20
elif bool(Dxie) == bool(Xxie) == 0:
    core = core + 0
else:
    core = core + 10

#数字
Num = re.findall(r'[0-9]',passwd)
if len(Num) == 0:
    core = core + 0
elif len(Num) == 1:
    core = core + 10
else:
    core = core + 20

#符号 33-47 58-64 91-96 123-126
Code = re.findall(r'[^A-Za-z0-9]',passwd)
if len(Code) == 0:
    core = core + 0
elif len(Code) == 1:
    core = core + 10
else:
    core = core + 25

#奖励reward
if (bool(Dxie) and bool(Xxie)) and bool(Num) and bool(Code):
    core = core + 5
elif bool(Dxie) != bool(Xxie) and bool(Num) and bool(Code):
    core = core + 3
elif bool(Dxie) != bool(Xxie) and bool(Num) and bool(Code) == 0:
    core = core + 2

#分级
if 90 <= core :
    print('VERY_SECURE')
elif 80 <= core < 90:
    print('SECURE')
elif 70 <= core <80:
    print('VERY_STRONG')
elif 60 <= core < 70:
    print('STRONG')
elif 50 <= core < 60:
    print('AVERAGE')
elif 25 <= core < 50:
    print('WEAK')
else:
    print('VERY_WEAK')