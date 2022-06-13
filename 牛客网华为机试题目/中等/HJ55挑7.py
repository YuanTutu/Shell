num=int(input())
count=[]
for i in range(1,num+1):
    if i%7 == 0:
        # print(i,"整除")
        count.append(i)
    else:
        for j in list(str(i)):
            if j == '7':
                # print(i, "包含7")
                if i not in count:
                    count.append(i)
                else:
                    pass
            else:
                # print(i,"no")
                pass
# print(count)
print(len(count))

# 大佬们的思路。count还能这么用……
# while True:
#     try:
#         n = int(input())
#         c = 0
#         for i in range(1,n+1):
#             if i % 7 == 0:
#                 c += 1
#             elif str(i).count('7') > 0 :
#                 c += 1
#         print(c)
#     except:
#         break
