n=int(input())
dcsl=[]
count=0
for i in range(0,n):
    dcsl.append(2+3*i)

for j in dcsl:
    count+=j

print(count)