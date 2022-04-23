# number = int(input())
# yueshu_list=[]
#
# # 求约数列表，这里已经把自身去掉了，range范围没有用number+1
# for i in range(1,number):
#     if number % i == 0:
#         yueshu_list.append(i)
# print(yueshu_list)
# # 求约数之和
# counter = 0
# for j in yueshu_list:
#     counter+=j
# print(counter)
# # 判断个数
# yue_count=0
# if counter==number:
#     yue_count+=1
# print(yue_count)

n = int(input())
# 一定要注意这个数组的位置，放在外面，不然总是会重置
yue_count = []
for number in range(1,n):
    yueshu_list=[]
    # 暴力计算求约数列表，这里已经把数字自身去掉了，range范围没有用number+1
    for i in range(1,number):
        if number % i == 0:
            yueshu_list.append(i)
    # print(yueshu_list)

    # 求约数之和
    counter = 0
    for j in yueshu_list:
        counter+=j
    # print(counter)

    # 有符合条件的数字就往数组里面+1
    if counter==number:
        yue_count.append(counter)

print(len(yue_count))



