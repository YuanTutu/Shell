# num1=str(input())
# num3=[]
# for i in num1:
#     num3.append(i)
# for j in num3[::-1]:
#     print(j,end='')

sentence = list(input().split())
print(sentence)

# 65-90 97-122
for i in sentence:
    for j in i:
        print(j,"=",ord(j))
        if ord(j)<=65:
            j = j.replace(j, '')
        elif 90<= ord(j) <=97:
            j = j.replace(j, '')
        elif ord(j) >= 122:
            j = j.replace(j, '')
        else:
            j=j
    print(j)
# for j in sentence[::-1]:
#     print(j,end=' ')
#