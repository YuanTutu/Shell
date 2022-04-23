import datetime
y,m,d=map(int,input().split())
# print(y,m,d)
d1=datetime.datetime(y,m,d)
d2=datetime.datetime(y,1,1)
result=d1-d2
print(result.days+1)