# -*- encoding: utf-8 -*-
"""
@File    : 14-常用的数据类型转换.py
@Time    : 2020/8/4 20:11
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

my_age = 28
print(type(my_age))

#强制将int类型数据转换成str类型数据
my_age = str(my_age)
print(type(my_age))

##eval用于计算字符串中有效的Python表达式，并且返回一个对象
my_height = '166.66'
my_height = eval(my_height)
print(type(my_height))
print(my_height)
