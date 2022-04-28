word = input()
word1=[]
for i in word:
    j=ord(i)
    word1.append(j)
counter = 0
for j in word1:
    if 65<= j <=90:
        counter+=1

print(counter)

# isupper() 据说也ok
