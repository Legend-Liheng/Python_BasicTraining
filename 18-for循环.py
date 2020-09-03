# -*- encoding: utf-8 -*-
"""
@File    : 18-for循环.py
@Time    : 2020/8/4 21:25
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

"""
    for循环和while循环的对比
"""

#range范围函数
for i in range(10):
    b = 1
    while b <= i:
        print("*", end="")
        b += 1
    print()

a = 1

while a < 10:
    b = 1
    while b <= a:
        print("*", end="")
        b += 1
    a += 1
    print()

