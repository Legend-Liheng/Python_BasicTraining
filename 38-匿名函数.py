# -*- encoding: utf-8 -*-
"""
@File    : 38-匿名函数.py
@Time    : 2020/8/13 17:52
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import random

#-----------------------无参数无返回值函数-----------------------
# #正常函数
# def my_pi():
#     print("hello python")
#
# my_pi()
#
# #匿名函数
# f = lambda : print("hello python")
# f()

#-----------------------无参数有返回值函数-----------------------
# #正常函数
# def my_pi():
#     return 10
#
# print(my_pi())
#
# #匿名函数
# f = lambda : 10
# print(f())

#-----------------------有参数无返回值函数-----------------------
# #正常函数
# def my_pi(a):
#     print(a)
#
# my_pi('李恒')
#
# #匿名函数
# f = lambda name : print(name)
#
# f('李恒')

#-----------------------有参数有返回值函数-----------------------
# #正常函数
# def my_pi(a, b):
#     return a + b
#
# print(my_pi(10, 20))
#
# #匿名函数
# f = lambda a, b: a + b
#
# print(f(10, 20))

#-----------------------嵌套调用函数-----------------------
# def fun(a, b):
#     return a + b

#直接调用函数
# def sum(a, b, c):
#     print(c(a, b))
#
# sum(10, 20, fun)

# #缺省参数调用函数
# def sum(a, b, c = fun):
#     print(c(a, b))

#直接调用函数
# def sum(a, b):
#     print(fun(a, b))
#
# sum(10, 20)

#-----------------------自定义排序（最外层肯定是列表）-----------------------
# my_dicts = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 19}, {'name': 'wangwu', 'age': 17}]
# print(my_dicts)
#
# #按照年龄排序
# my_dicts.sort(reverse= True, key=lambda x: x['age'])#思考：为什么可以通过lambda my: my['age']进行排序？？？
# print(my_dicts)
#
# #按照姓名排序
# my_dicts.sort(key=lambda x: x['name'])#按照ASCII码值进行排序
# print(my_dicts)

my_list = []
all_list = []

for i in range(3):
    for j in range(4):
        j = random.randint(-100, 100)
        my_list.append(j)
        # print(j)

    all_list.append(my_list)
    my_list = []

print(all_list)

#按小列表第一位排序
all_list.sort()
print(all_list)

#按小列表最后一位排序
all_list.sort(key= lambda list: list[-1])
print(all_list)




