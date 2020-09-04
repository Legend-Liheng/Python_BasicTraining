# -*- encoding: utf-8 -*-
"""
@File    : 26-列表的元素添加.py
@Time    : 2020/8/8 16:11
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

my_list = [123, 'hello', 'python', [0, 1]]

# help(list)

my_list.append(["添加的新元素"])
# print(list.__add__(my_list, ["添加的新元素"]))
print(my_list)

#添加一个可以遍历的对象
# my_list.extend([1, 2, 3])
# print(my_list)

#在第X位插入XX元素
my_list.insert(20, 2)
print(my_list)

my_list[1] = "hahaha"
print(my_list)

# if 'hahaha' not in my_list:
#     print('hahaha在my_list列表中')
# elif '123' not in my_list:
#     print('asdf')

#删除指定下标索引的元素
del my_list[1]
print(my_list)

#删除最后一个元素
print(my_list.pop(2))
print(my_list)

