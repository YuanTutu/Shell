# -*- coding=utf-8 -*-
#异步爬虫的方式
#多线程，多进程（不建议使用）：
#好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步执行
#弊端：无法无限制的开启多线程或者多进程
#线程池，进程池：
#好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统的开销
#弊端：池中线程或进程的数量是有上限的

import requests
import time

# #单线程串行案例，模拟下载
# def get_page(str):
#     print("正在下载： ",str)
#     time.sleep(2)
#     print("下载成功： ",str)
# name_list = ['xiaozi','aa','bb','cc']
# start_time = time.time()
# for i in range(len(name_list)):
#     get_page(name_list[i])
# end_time = time.time()
# print('%d second'%(end_time-start_time))

# #使用线程池方式执行，导入新模块
# from multiprocessing.dummy import Pool
# start_time = time.time()
# def get_page(str):
#     print("正在下载： ",str)
#     time.sleep(2)
#     print("下载成功： ",str)
# name_list = ['xiaozi', 'aa', 'bb', 'cc']
# #实例化一个线程池对象
# pool=Pool(4)
# #将列表中每一个元素给get_page进行处理
# pool.map(get_page,name_list)
# # for i in range(len(name_list)):
# #     get_page(name_list[i])
# end_time = time.time()
# print('%d second'%(end_time-start_time))

