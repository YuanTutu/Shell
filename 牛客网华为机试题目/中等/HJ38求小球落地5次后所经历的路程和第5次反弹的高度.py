hight = int(input())
origin_h=hight
l1=[]

for i in range(1,7):
    # print(i)
    l1.append(hight)
    hight = hight/2
# print(l1)

l2=0
for i in l1[:4]:
    # print(i)
    l2=l2+i

print(l2+origin_h)
print(l1[-1])