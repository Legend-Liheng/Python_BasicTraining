# -*- encoding: utf-8 -*-
"""
@File    : 22-字符串的操作.py
@Time    : 2020/8/5 14:16
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

str = 'abcasdfsfssdfs'

#find查找，并返回该元素的第一个下标，如果没有则返回-1
print(str.find('f'))
print(str.find('k'))

#index查找，类似find，并返回该元素的第一个下标，如果没有则会报错
print(str.index('f'))
# print(str.index('k'))

#count统计元素在出现的此事
print(str.count('f'))

#replace替换，如果指定count，则替换不超过count次
str = str.replace('f', 'k', 1)
print(str)

#split
print(str.split('f'))

help(str)
