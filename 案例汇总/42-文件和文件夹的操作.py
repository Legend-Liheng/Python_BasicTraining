# -*- encoding: utf-8 -*-
"""
@File    : 42-文件和文件夹的操作.py
@Time    : 2020/8/16 9:18
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import os

#重命名
# os.rename('test.txt', '李恒.txt')

#删除文件
# os.remove('liheng.txt')

#删除目录
os.removedirs('逍遥1')
os.rmdir()

#创建目录
os.mkdir('逍遥1')

#获取当前目录
ret = os.getcwd()
print(ret)

#获取当前目录所有文件/文件夹
ret = os.listdir()
print(ret)#.idea为隐藏文件


