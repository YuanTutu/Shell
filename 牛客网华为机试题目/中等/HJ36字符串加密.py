key = list(input())
passwd = input()

#处理秘钥
set1=set([])
keyword=''
for i in range(len(key)):
    if key[i] not in set1:
        keyword=keyword+key[i]
        set1.add(key[i])

ALL='abcdefghijklmnopqrstuvwxyz'
replaceall=[]
for i in ALL:
    if i not in keyword:
        replaceall.append(i)
#新的秘钥
NEWALL=list(keyword)+replaceall

#查找待处理的字符在ALL中的位置：
for i in passwd:
    a = ALL.index(i)
    print(NEWALL[a],end='')