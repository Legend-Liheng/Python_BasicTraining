# -*- encoding: utf-8 -*-
"""
@File    : 50-获取异常.py
@Time    : 2020/8/28 10:32
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    常见获取异常方法
    try……except……else……finally……
'''
#执行可能会抛出异常的代码
try:
    # open('text.txt', 'r')
    # open('复制.txt', 2)
    print(haha)
    # print('哈哈')

#如果有异常则执行该代码，获取异常信息，并且抛出显示
except (FileNotFoundError, BaseException) as a:
    print('异常详情：', a)

#如果没有异常，则执行以下内容
else:
    print('无异常')

#不管有没有异常，该代码都会执行
finally:
    print('不管有没有异常，我都执行')

#try的嵌套
try:
    try:
        print(haha)
    finally:
        print('里面的；异常')
except NameError as a:
    print('获取异常：', a)



















