# s1,s2=input(),input()
# # print(s1)
# # print(s2)
# counter=0
# for i in s1:
#     for j in s2:
#         if i == j:
#             counter+=1
#
# print(counter)
# if counter==len(s1):
#     print("true")
# else:
#     print("false")

# 震惊，交并差
while True:
    try:
        S, T = input(), input()
        if set(S) & set(T) == set(S):
            print('true')
        else:
            print('false')
    except:
        break
