# -*- encoding: utf-8 -*-
"""
@File    : 43-批量修改文件名.py
@Time    : 2020/8/16 10:35
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import os

#创建一个根目录
# os.mkdir('批量修改文件名')
#
#更改当前目录
# os.chdir('批量修改文件名')
#
# for i in range(10):
#     file_name = ('%d.txt'% i)
#     f = open(file_name, mode='w',encoding= 'UTF-8')
#
#     file_content = ('我是第%d个内容'% i)
#     f.write(file_content)

#获取当前工作目录
print(os.getcwd())

#修改当前工作目录
os.chdir('批量修改文件名')
print('修改后的工作目录为：', os.getcwd())

#新建一个列表，保存对应目录下的所有文件
my_list = os.listdir()
print(my_list)

#i为列表下标索引
for i, txt_name in enumerate(my_list):
    # new_name = txt_name.replace('.txt', '中国.txt')
    new_name = os.rename(txt_name, '%d中国人.txt' % i)

new_name = os.listdir()
print(new_name)