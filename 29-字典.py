# -*- encoding: utf-8 -*-
"""
@File    : 29-字典.py
@Time    : 2020/8/9 9:22
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

my_dict = {'username' : 10000, 'password' : 'Aa123456'}

print(my_dict['username'])

#修改值
my_dict['username'] = 13735
print(my_dict['username'])

#添加键值
my_dict['url'] = 'www.baidu.com'
print(my_dict)

#删除
del my_dict['url']
print(my_dict)

# #清空
# my_dict.clear()
# print(my_dict)

#返回键值的数量
print(len(my_dict))

#返回键值
print(my_dict.keys())

#返回实值
print(my_dict.values())


