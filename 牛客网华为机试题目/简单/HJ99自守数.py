# 自守数是指一个数的平方的尾数等于该数自身的自然数。
# 例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376
n=int(input())
count=0

for i in range(0,n+1):
    j=str(pow(i,2))#计算平方数
    l=j[-len(str(i)):]
    if str(i) == l:
        count+=1

print(count)

