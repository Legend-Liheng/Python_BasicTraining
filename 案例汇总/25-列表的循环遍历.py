# -*- encoding: utf-8 -*-
"""
@File    : 25-列表的循环遍历.py
@Time    : 2020/8/8 15:59
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
# str = "hello"
#
# for c in str:
#     print(c)

list = [123, 'hello', 'python', [0, 1]]

"""
    可以看出，for循环语句更好用
"""
#遍历列表的元素
for c in list:
    print(c)

index = 0
#遍历列表的元素
while index < len(list):
    print(list[index])
    index += 1