a = input()
resoult={}
for j in a:
    resoult[j] = a.count(j)

# 再次遍历去掉次数最少的
for j in resoult.keys():
    # 判断等于最小的次数  min(d.values())
    if resoult[j] == min(resoult.values()):
        a = a.replace(j, '')
print(a)
