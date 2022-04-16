a = list(input())
b = []
#先把字符都转换成ascii
for i in a:
    b.append(ord(i))
c=[]
#死亡if
# 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0
for j in b:
    if 65 <= j <=89:
        j=j+1
        c.append(chr(j).lower())
    elif j == 90:
        j=j-25
        c.append(chr(j).lower())
    elif 97<= j <=99:
        c.append(2)
    elif 100<= j <=102:
        c.append(3)
    elif 103<= j <=105:
        c.append(4)
    elif 106<= j <=108:
        c.append(5)
    elif 109<= j <=111:
        c.append(6)
    elif 112<= j <=115:
        c.append(7)
    elif 116<= j <=118:
        c.append(8)
    elif 119<= j <=123:
        c.append(9)
    else:
        c.append(chr(j))

for k in c:
    print(k,end="")