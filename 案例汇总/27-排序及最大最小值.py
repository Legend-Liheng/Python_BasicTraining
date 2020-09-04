# -*- encoding: utf-8 -*-
"""
@File    : 27-排序.py
@Time    : 2020/8/8 16:50
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
import random

my_list = []

for c in range(6):
    value = random.randint(-100, 100)
    my_list.append(value)

print(my_list)

# #从小到大排序
# my_list.sort()
# print(my_list)
# print('最小值为：', my_list[0])
# print('最大值为：', my_list[len(my_list)-1])
#
# #从大到小排序
# my_list.sort(reverse = True)
# print(my_list)
# print('最大值为：', my_list[0])

#通过遍历，获取最小值
min_value = my_list[0]

for i in my_list:
    if i < min_value:
        min_value = i
        # print(min_value)

print(min_value)
