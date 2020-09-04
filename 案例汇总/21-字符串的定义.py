# -*- encoding: utf-8 -*-
"""
@File    : 21-字符串的定义.py
@Time    : 2020/8/5 8:32
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

# my_str = '你好啊' \
#          '好好好' \
#          '好的哼'
#
# print(my_str)
#
# my_str = """你好啊
# 好好好
# 好的哼"""
#
# print(my_str)

str = 'hello python'

#左索引
print(str[2])
# print(str[0, 3])

#右索引
print(str[-1])

print(len(str))

for i in range(5):
    print(str[i])
    i += 1

print(str[:4])