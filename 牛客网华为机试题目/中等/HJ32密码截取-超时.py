str = input()
n = len(str)
list = []
for i in range(0,n-1):
    for j in range(1,n):
        if str[j] == str[i] and str[i+1:j] == str[j-1:i:-1]:
            list.append(len(str[i:j+1]))
print(max(list))