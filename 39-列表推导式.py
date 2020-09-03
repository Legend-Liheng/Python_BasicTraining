# -*- encoding: utf-8 -*-
"""
@File    : 39-列表推导式.py
@Time    : 2020/8/14 20:53
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

# my_list = []

#创建一个从1到30的列表
# for i in range(1, 31):
#     my_list.append(i)
#
# print(my_list)

# my_list = [i for i in range(1, 31)]
# print(my_list)

#创建30个哈哈
# for i in  range(30):
#     my_list.append('哈哈')
#
# print(my_list)
#
# my_list = ['哈哈' for i in range(30)]
# print(my_list)

# #创建1~30以内的偶数列表
# for i in range(1, 30):
#     if i % 2 == 0:
#         my_list.append(i)
#
# print(my_list)

my_list = [i for i in range(1, 30) if i % 2 == 0]
print(my_list)



