# 注释的内容是把字符转换成ASCII码再比较，但有点多此一举了

word=input()
# trans=[]
# for i in list(word):
#     trans.append(ord(i))
resoult={}
# for j in trans:
#     resoult[j] = trans.count(j)
for j in word:
    resoult[j] = word.count(j)
print(len(resoult))


