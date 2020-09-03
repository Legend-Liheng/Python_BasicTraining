# -*- encoding: utf-8 -*-
"""
@File    : 52-txt文件的读取.py
@Time    : 2020/8/28 14:43
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

# # 以只读模式打开文件
# f = open('test.txt', 'r', encoding= 'UTF-8')
#
# # 读取文件中的数据
# print(f.read())
#
# #关闭文件，释放内存
# f.close()

with open('test.txt', 'r', encoding= 'UTF-8') as f:
    print(f.read())


