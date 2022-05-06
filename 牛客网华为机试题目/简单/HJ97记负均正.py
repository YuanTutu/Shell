n = int(input())
number = input().split()
zhengshu=0
count=0
fushu=0
for i in number:
    if int(i) > 0:
        count += int(i)
        zhengshu += 1
    elif int(i) < 0 :
        fushu += 1
if zhengshu!=0:
    result=count/zhengshu
    print(fushu, "%.1f" % result)
else:
    print(fushu,"0.0")
