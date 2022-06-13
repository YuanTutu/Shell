word = input()
dict={}
for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1

d1 = dict.values()

count=0
for j in d1:
    if j != 1:
       count+=1
    elif j == 1:
       print(list(dict.keys())[list(dict.values()).index(1)])
       break
if count==len(d1):
    print("-1")

