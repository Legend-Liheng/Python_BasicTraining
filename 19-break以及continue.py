# -*- encoding: utf-8 -*-
"""
@File    : 19-break以及continue.py
@Time    : 2020/8/4 21:36
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

#break是结束循环
for i in range(5):

    if i == 3:
        break
    print(i)

#continue是不执行后续代码
for i in range(5):

    if i == 3:
        continue
    print(i)



