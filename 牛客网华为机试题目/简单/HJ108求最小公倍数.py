
a,b=map(int,input().split())
if a > b:
    bigger=a
else:
    bigger=b
while True:
    if bigger%a==0 and bigger%b==0:
        lcm=bigger
        break
    else:
        # 运行超时，改成+b就不超时了
        # bigger+=1
        bigger+=b
print(lcm)
# 灵感来源
# while True:
#     try:
#         a,b=list(map(int, input().split()))
#         if a < b:
#             a,b=b,a
#         for i in range(a,a*b+1,a):
#             if i%b==0:
#                 print(i)
#                 break
#     except:
#         break


