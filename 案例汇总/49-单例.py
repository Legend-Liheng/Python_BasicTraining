# -*- encoding: utf-8 -*-
"""
@File    : 49-单例.py
@Time    : 2020/8/27 14:28
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    单例模式中程序在这个类创建创建出来的对象，只有一个（即占用一份内存地址）
    __new__方法在单例中的应用
'''

class Num():

    # 定义一个类属性，保存这个类创建的对象
    instance = None 

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)

        return cls.instance

    def __init__(self, a, b):
        print('%d + %d = %d' %(a, b, a + b))

num1 = Num(10, 20)
print(num1)

num2 = Num(2, 3)
print(num2)

