a=input()
english=[]
space=[]
number=[]
other=[]
for i in a:
    # print(i,end=' ')
    if i.isalpha():
        english.append(i)
    elif i.isdigit():
        number.append(i)
    elif ord(i) == 32:
        space.append(i)
    else:
        other.append(i)
print(len(english))
print(len(space))
print(len(number))
print(len(other))
