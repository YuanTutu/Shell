#-*- coding:utf-8 -*-
def huiwenshu(x):
    str_x = str(x)
    str_y = ""
    for i in str_x:
        str_y = i + str_y
        print(str_y)
    return str_y == str_x

if __name__ == '__main__':
    x = input("回文数：>>>")
    y = huiwenshu(x)
    print(y)
