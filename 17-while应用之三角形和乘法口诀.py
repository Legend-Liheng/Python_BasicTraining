# -*- encoding: utf-8 -*-
"""
@File    : 17-while应用之打印一个三角形.py
@Time    : 2020/8/4 21:02
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

"""
    打印三角形
"""
a = 1

while a < 10:
    b = 1
    while b <= a:
        print("*", end="")
        b += 1
    a += 1
    print("")

"""
    打印9*9乘法表
"""

a = 1

while a <= 9:
    b = 1

    while b <= a:
        print("%d * %d = %d  " % (b, a, b * a), end='')
        b += 1
    print()
    a += 1

