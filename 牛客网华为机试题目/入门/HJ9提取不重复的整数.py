num=str(input())
val=[]
for i in num[::-1]:
    if i not in val:
        val.append(i)
if val[0] == '0':
    val.pop(0)
    print(''.join(val))
else:
    print(''.join(val))