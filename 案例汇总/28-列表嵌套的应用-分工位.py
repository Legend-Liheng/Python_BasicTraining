# -*- encoding: utf-8 -*-
"""
@File    : 28-列表嵌套的应用-分工位.py
@Time    : 2020/8/8 17:12
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
import random

my_list = [[], [], []]
techer = 'ABCDEFGH'

for i in techer:
    value = random.randint(0, 2)
    my_list[value].append(i)

print(my_list)





