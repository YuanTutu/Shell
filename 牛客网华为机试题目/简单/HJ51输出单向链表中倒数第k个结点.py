while True:
    try:
        a=int(input())
        b=[]
        c=input()
        d=int(input())
        for i in c.split():
            b.append(i)
        print(b[-d])
    except:
        break

# 下面是大佬们的做法
# 第一种
# 无脑列表
# while True:
#     try:
#         count, num_list, k = int(input()), [int(x) for x in input().split()], int(input())
#         print(num_list[-k] if k else 0)
#     except EOFError:
#         break

# 第二种
# 纯链表
#
# class Node(object):
#     def __init__(self, val=0):
#         self.val = val
#         self.next = None
#
#
# while True:
#     try:
#         head = Node()
#         count, num_list, k = int(input()), list(map(int, input().split())), int(input())
#         while k:
#             head.next = Node(num_list.pop())
#             head = head.next
#             k -= 1
#         print(head.val)
#     except EOFError:
#         break
