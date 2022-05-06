#看看大佬们的做法吧
import re
def func(s):
    str1 = re.sub('[0-9]+','*\g<0>*',s)
    print(str1)
while 1:
    try:
        func(input())
    except:
        break
#第二种方法
while True:
    try:
        s = input()
        s_o = ''
        char_pre = ''
        for i in s:  # 遍历字符串
            if i.isdigit():  # 遇到数字，判断其前面是否非数字，是则表示数字的开始，先插入‘*’
                if char_pre.isdigit() != True:
                    s_o += '*'
            else:  # 非数字情况，判断其前是否为数字，是则表示数字结束，插入‘*’
                if char_pre.isdigit():
                    s_o += '*'
            s_o += i  # 把当前字符带出来
            char_pre = i  # 当前字符更新到 前字符
        if i.isdigit():  # 结束的时候，判断是否数字结束，如果是的话，插入‘*’
            s_o += '*'
        print(s_o)
    except:
        break

