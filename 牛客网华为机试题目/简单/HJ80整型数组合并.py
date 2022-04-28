a=int(input())
lista=list(map(int,input().split()))
b=int(input())
listb=list(map(int,input().split()))
# 其实想想就是去重不知道set这个东西……
# for i in lista:
#     for j in listb:
#         if i == j :
#             lista.remove(i)
# listc=sorted(lista+listb)
listc=sorted(set(lista+listb))
for i in listc:
    print(i,end="")

# 没看懂set是咋操作去重，百度搜索说是set自动去重
# 创建一个无序不重复元素的集合 ，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。其返回值为一个新的集合对象。
# while 1:
#     try:
#         s0,s1,s3,s2 = input(), input().split(), input(), input().split()
#         s = map(str,sorted(map(int, set(s1+s2))))
#         print(''.join(s))
#     except:
#         break

# 类似的操作
# while True:
#     try:
#         first_num = int(input())
#         first_list = list(map(int, input().split(" ")))
#         second_num = int(input())
#         second_list = list(map(int, input().split(" ")))
#
#         total_list = first_list + second_list
#         total_list = list(set(total_list))
#         total_list.sort()
#         res = ''.join(list(map(str, total_list)))
#         print(res)
#     except EOFError:
#         break
