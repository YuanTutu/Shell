num=int(input())
count=[]
for i in range(1,num+1):
    if i%7 == 0:
        print(i,"整除")
        count.append(i)
    else:
        for j in list(str(i)):
            if j == '7':
                print(i, "包含7")
                if i not in count:
                    count.append(i)
                else:
                    pass
            else:
                print(i,"no")
print(count)
print(len(count))

