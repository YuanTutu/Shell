# for in 循环
"""
求1-100的和
"""
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

"""
用for循环求1-100偶数和
"""
# sum = 0
# for i in range(1,101):
#     if i%2 == 0:
#         sum += i
# print(sum)

# while循环
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random
#
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number < answer:
#         print("大一点")
#     elif number > answer:
#         print("小一点")
#     else:
#         print("恭喜你才对了")
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('多练练')

"""
九九乘法表
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d * %d = %d' %(i,j,i*j),end = '\t')
#     print()

# 练习
"""
判断是不是素数
开根号法。可以参考：https://blog.csdn.net/zhao2chen3/article/details/82955794
"""
# from math import sqrt
#
# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# print(end)
# is_prime = True
# for x in range(2,end+1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

"""
输入两个正整数，计算最大公约数和最小公倍数
"""
# x=int(input('x='))
# y=int(input('y='))
# if x > y:
#     x,y=y,x
#     # print(x,y)
# #从x开始取每次-1到0，但不包括0
# for factor in range(x,0,-1):
#     if x % factor == 0 and y % factor == 0:
#         print("%d 和 %d 的最大公约数是 %d" % (x,y,factor))
#         # 向下//取整除
#         print("%d 和 %d 的最小公倍数是 %d" % (x,y,x*y//factor))
#         break

"""
打印各种三角形
"""
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()