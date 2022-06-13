n=int(input())
m=input().split()#重量
x=input().split()#数量

result=[]
for i in range(n):
    for j in range(int(x[i])):
        result.append(int(m[i]))
# print(result)

count={0}
for i in result:
    for j in list(count):
        count.add(i+j)
# print(count)
print(len(count))

