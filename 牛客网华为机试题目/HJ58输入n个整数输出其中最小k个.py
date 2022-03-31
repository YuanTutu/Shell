n,k=input().split()
arr = input("")
num = [int(i) for i in arr.split()]
# print(n,type(n))
# num.sort()
# print(num[:int(k)])
if len(num) == int(n):
    num.sort()
    for i in range(0, int(k)):
        print(num[i],end=" ")
else:
    print(len(num))

