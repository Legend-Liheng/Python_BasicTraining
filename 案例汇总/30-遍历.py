# -*- encoding: utf-8 -*-
"""
@File    : 30-遍历.py
@Time    : 2020/8/9 9:32
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    分别对字符串、列表、元组、字典进行遍历
'''

# my_char = 'abcdefg'
# for c in my_char:
#     print(c)

# my_list = [123, 'haha', '李恒', [4, 5]]
# for l in my_list:
#     print(l)

# my_tuple = (123, 'haha', '李恒', [4, 5])
# for t in my_tuple:
#     print(t)

my_dict = {'数字': 123, '字母' : 'haha', '中文' : '李恒', '列表' : [4, 5]}
for d in my_dict.keys():
    print(d)

for d in my_dict.values():
    print(d)

for d in my_dict.items():
    print(d)

for key, value in my_dict.items():
    print('key:', key)
    print('value:', value)

#获取一个列表元素以及对应的下标索引
my_list = 'abcd'
for i, value in enumerate(my_list):
    print(i, value)
