# n = int(input())
# list = [[0]]*n
# for i in range(int(n)):
#     list[i] = input().split()
#     list[i] = [int(j) for j in list[i]]
# print(list)
# result=[]
# for a in list:
#     print(a)

n = int(input())
dic = {}

# idea: 动态建构字典
for i in range(n):
    line = input().split()
    # print(line[0],line[1])
    key = int(line[0])
    value = int(line[1])
    dic[key] = dic.get(key, 0) + value  # 累积key所对应的value
for each in sorted(dic):  # 最后的键值对按照升值排序
    print(each, dic[each])
