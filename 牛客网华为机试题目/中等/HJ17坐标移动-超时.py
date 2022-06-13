while True:
    try:
        step = input().split(";")
        step3=[]
        step4=[]
        origin=[0,0]

        for i in step:
            if len(i)==3 and i[0] in ("A","S","D","W") and i[1].isdigit() and i[2].isdigit():
                step3.append(list(i))
            else:
                pass

        for i in step3:
            j=i[1]+i[2]
            i.remove(i[1])
            i.remove(i[1])
            i.append(int(j))
            step4.append(i)

        for i in step4:
            if i[0] == 'A':
                origin[0]-=i[1]
            elif i[0] =='S':
                origin[1]-=i[1]
            elif i[0] == 'D':
                origin[0]+=i[1]
            elif i[0] == 'W':
                origin[1]+=i[1]
            else:
                pass

        print(origin[0],",",origin[1])


    except:
        pass

# 大佬的题解
# input_list = input().split(';')
# initial = [0,0]
#
# for item in input_list:
#     if not 2 <= len(item) <= 3:
#         continue
#
#     try:
#         direction = item[0]
#         step = int(item[1:])
#         if direction in ['A', 'D', 'W', 'S']:
#             if 0 <= step <= 99:
#                 if direction == 'A':
#                     initial[0] -= step
#                 elif direction == 'D':
#                     initial[0] += step
#                 elif direction == 'S':
#                     initial[1] -= step
#                 elif direction == 'W':
#                     initial[1] += step
#     except:
#         continue
#
# print(str(initial[0]) + ',' + str(initial[1]))