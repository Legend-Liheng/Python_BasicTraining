# -*- encoding: utf-8 -*-
"""
@File    : 34-函数.py
@Time    : 2020/8/9 15:01
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

"""
    四种函数类型
    01-无参数无返回值
    02-无参数有返回值
    03-有参数无返回值
    04-有参数有返回值
"""

#常见函数调用
def add_2_num(a, b):
    return a + b

print(add_2_num(1, 3))

#计算三个数的和，位置参数
def sum(a, b, c):
    sum = a + b + c
    # print('%d + %d + %d = %d'% (a, b, c, sum))
    return  sum

sum1 = sum(1, 2, 3)
print(sum1)

#计算三个数的平均数,关键字参数
def average(a, b, c):

    average = (a + b + c) / 3
    # print("%d、%d、%d三者平均数为%.2f" % (a, b, c, average))
    return average

ave1 = average(a= 1, b= 2, c= 3)
print(ave1)

#计算三个数的乘积，缺省参数
def product(a, b, c = 100):
    pro = a * b * c
    return pro

pro1 = product(4, 5)
print(pro1)