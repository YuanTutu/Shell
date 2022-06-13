def check_pass(passwd):
    if len(passwd) < 8:
        return 0
    daxie = xiaoxie = shuzi = fuhao = 0
    for i in passwd:
        if ord('A') <= ord(i) <= ord('Z'):
            daxie = 1
        elif ord('a') <= ord(i) <= ord('z'):
            xiaoxie = 1
        elif ord('0') <= ord(i) <= ord('9'):
            shuzi = 1
        else:
            fuhao = 1
    sum = daxie + xiaoxie + shuzi + fuhao
    if sum < 3:
        return 0
    for i in range(len(passwd) - 3):
        if len(passwd.split(passwd[i:i + 3])) >= 3:
            return 0
    return 1
    # 字典也很绝啊……
    # dc = {}
    # for i in range(len(pw) - 2):  # 遍历所有的子字符串起点
    #     if pw[i:i + 3] in dc:  # 在字典中搜索
    #         return False
    #     else:  # 如果未曾经出现过则加入字典中，等待之后的判定
    #         dc[pw[i:i + 3]] = 1
    #
    # return True

while True:
    try:
        passwd=input()
        if check_pass(passwd):
            print("OK")
        else:
            print("NG")
    except:
        break