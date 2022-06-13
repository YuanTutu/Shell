shuru = input().split()
list1=[]
list1.append(shuru[1])
list2=shuru[2:-1]
waitfordelete=shuru[-1]

# 5 2 3 2 4 3 5 2 1 4 3
# 2->5->3->4->1
for i in range(1,len(list2),2):
    list1.insert(list1.index(list2[i]),list2[i-1])

list3=list1[::-1]

for i in list3:
    if i != waitfordelete:
        print(i,end=' ')
    else:
        pass
