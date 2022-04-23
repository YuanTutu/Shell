# 公鸡5
# 母鸡3
# 3小鸡1
a = input()
for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        if 5*x+3*y+z/3==100:
            print(x,y,z)


# import random
# num=input()
# while True:
#    x=random.randrange(0,20)
#    y=random.randrange(0,33)
#    z=random.randrange(0,100)
#    if 5*x+3*y+z/3==100 and x+y+z==100:
#        print(x,y,z)
