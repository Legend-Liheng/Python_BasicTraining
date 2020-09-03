# -*- encoding: utf-8 -*-
"""
@File    : 41-文件的操作.py
@Time    : 2020/8/16 7:26
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

file_name = '文件/test.txt'

# f = open(file_name, mode= 'a+', encoding= 'UTF-8')
# f.write('你好啊1')

f1 = open(file_name, mode= 'r', encoding= 'UTF-8')
# f.write('我爱你')
ret = f1.read()
print(ret)

f2 = open('复制.txt', mode= 'w+', encoding= 'UTF-8')
f2.write(ret)
print(f2.read())
print(f2.tell())

f1.close()
f2.close()
