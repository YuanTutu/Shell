N=int(input())
namelist=[]
for i in range(N):
    namelist.append(input())

for i in namelist:
    dict = {}# 创建字典，键是字母，值是数量
    for j in i:
        if j not in dict:
            dict[j] = 1
        else:
            dict[j] = dict[j] + 1
    d1 = sorted(dict.values(),reverse=True)
    ans = 0
    m = 0
    for i in d1:
        ans = ans + (26 - m)*i
        m+=1
    print(ans)


