# ASCII码表
# 0-9  48-57
# A-Z 65-90
# a-z 97-122
a=input()
b=[]
for i in a:
    b.append(ord(i))
# print(b)
c=sorted(b)
for j in c:
    print(chr(j),end='')