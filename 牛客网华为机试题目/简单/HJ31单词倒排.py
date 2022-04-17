# # num1=str(input())
# # num3=[]
# # for i in num1:
# #     num3.append(i)
# # for j in num3[::-1]:
# #     print(j,end='')
#
# sentence = list(input().split())
# print(sentence)
# ok=[]
# # 65-90 97-122
# for i in sentence:
#     for j in i:
#         print(j,"=",ord(j))
#         if ord(j)<65:
#             j = j.replace(j, ' ')
#             ok.append(j)
#         elif 90< ord(j) <97:
#             j = j.replace(j, ' ')
#             ok.append(j)
#         elif ord(j) > 122:
#             j = j.replace(j, ' ')
#             ok.append(j)
#         else:
#             ok.append(j)
# print(ok)
# # for j in sentence[::-1]:
# #     print(j,end=' ')
#以上是我的傻叉操作……尝试了一些做法
#纯句子可以直接倒序排列，但加上符号啥的我就没琢磨明白
#我尝试了ascii码判断是否是字母啥的，能替换但是结构散了……
#直到我发现，他么的又是带内置函数，下次干脆先搜搜能不能用内置函数吧
#下面是大佬写的代码
s=input()
for i in range(len(s)):#将所有非字母字符替换为空格
    if not s[i].isalpha():#注意字符串自带函数用法，否则较难实现
        s = s.replace(s[i],' ')
s = s.split(' ')
s = s[::-1]
print(' '.join(s))
