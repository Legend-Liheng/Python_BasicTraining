# -*- encoding: utf-8 -*-
"""
@File    : 40-文件的打开与关闭.py
@Time    : 2020/8/14 21:11
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

# help(open)

file_name = "test.txt"

#写
# f = open(file_name, "w", encoding= 'UTF-8')
# f.write('我爱老婆')

#读
# f = open(file_name, "r", encoding= 'UTF-8')
# ret = f.read()
# print(ret)

f = open(file_name, 'r+', encoding= 'UTF-8')
# ret = f.write('今天天气很好1\n')
ret1 = f.readlines()

# print(ret)
print(ret1)

#读取全部
# ret = f.read()
# print(ret)

#读取部分
# ret = f.read(2)
# print(ret)

ret = f.readlines()
print(ret)

#关闭文件，释放内存
f.close()




