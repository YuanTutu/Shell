# 杨辉三角是歌什么姬吧
while True:
    try:
        # 行数
        n = int(input())
        def func(n):
            if n <= 2:
                return -1
            elif n%2 == 1:
                return 2
            else:
                return int(n/2%2+3)
        print(func(n))
    except:
        break