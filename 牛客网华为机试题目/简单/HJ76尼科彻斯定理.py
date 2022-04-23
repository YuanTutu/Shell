m=int(input())
list=[]
if 1<= m <= 100:
    n=m**2+(m-1)
    list.append(n)
    for i in range(1,m):
        n=n-2
        list.append(n)
# print(list)
list.reverse()
for j in list[0:-1]:
    print(j,end="")
    print("+",end="")
print(list[-1])