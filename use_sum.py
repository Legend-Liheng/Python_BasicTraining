# -*- encoding: utf-8 -*-
"""
@File    : use_sum.py
@Time    : 2020/8/28 13:44
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    常用方法1：import 模块名
    调用规则：模块名.属性名   模块名.函数名   模块名.类名
'''

# import custom_sum
#
# print(custom_sum.name)
# print(custom_sum.sum(10, 20))
# custom_sum.Person().eat()

'''
    常用方法2：import 模块名 as 自定义模块名
    调用规则：自定义模块名.属性名  自定义模块名.函数名  自定义模块名.类名
'''

# import custom_sum as sum
#
# print(sum.name)
# print(sum.sum(20,40))
# sum.Person().eat()

'''
    常用方法3：from 模块名 import 属性名, 函数名, 类名
    调用规则：直接填写属性名  函数名  类名进行调用
    缺点：会和本模块内的同名属性、函数、类名起冲突
'''

# from custom_sum import name, sum, Person
#
# print(name)
# print(sum(10, 10))
# Person().eat()

'''
    常用方法4：from 模块名 import 属性名 as 自定义属性名
    调用规则：直接填写自定义属性名进行调用
'''

from custom_sum import name as myname
print(myname)

'''
    常用方法5：from 模块名 import *
    调用规则：直接填写属性名  函数名  类名进行调用
    对比方法3的优点：不用枚举导入模块中的属性、函数、类名
'''

# from custom_sum import *
#
# print(name)
# print(sum(20, 20))
# Person().eat()

'''
    常用方法6：import 模块1， 模块2……
    优点：省略行数，简洁
'''


