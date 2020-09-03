# -*- encoding: utf-8 -*-
"""
@File    : 37-局部变量和全局变量.py
@Time    : 2020/8/13 17:38
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
#定义全局变量
var = 13

#定义局部变量
def local_var():
    var = 12
    print('里面', var)

def global_var():
    print('外面', var)

local_var()
global_var()

#对全局变量金额进行修改
def change_global_var():
    global var

    var = 100
    print('修改后的全局变量值为：', var)

change_global_var()
