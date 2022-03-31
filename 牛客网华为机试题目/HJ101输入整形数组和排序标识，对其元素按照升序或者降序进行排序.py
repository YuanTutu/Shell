# 输入整形数组和排序标识，对其元素按照升序或者降序进行排序
# 方法1
while True:
    try:
        a,b,c=input(),map(int,input().split()),input()
        print(" ".join(map(str,sorted(b))) if c=="0" else " ".join(map(str,sorted(b,reverse=True))))
    except:
        break

# 方法2
n = int(input())
val = input().split()
sign = int(input())
val_1 = list(map(int,val))
if sign == 0:
    val_1.sort()
    for i in range(0,len(val_1)):
        print(val_1[i],end=" ")
elif sign == 1:
    val_1.sort(reverse=True)
    for i in range(0,len(val_1)):
        print(val_1[i],end=" ")