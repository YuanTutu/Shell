n = int(input())
name = input().split()
m = int(input())
piao = input().split()

valid=[]
for i in name:
    count = piao.count(i)
    valid.append(count)
    print(i,":",count)
number=0
for j in valid:
    number+=j
print("Invalid :",m-number)