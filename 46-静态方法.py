# -*- encoding: utf-8 -*-
"""
@File    : 49.py
@Time    : 2020/8/19 15:28
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    为什么要使用静态方法
    静态方法既不访问成员变量，也不访问类变量，若写个和class同级别的def函数也能实现同样的功能，何必定义个静态方法呢？定义静态方法主要是规避两个模块调用同名函数的情况，

    假设一个场景：为Car类定义一个同级别的def tips函数，再为Animal类定义一个同级别的def tips函数
'''

# class Car(object):
#     pass
#
# def tips():
#     print("温馨提示：开车不喝酒")
#
# class Animal(object):
#     pass
#
# def tips():
#     print("温馨提示：不要伸手投食")
#
# tips()

#在python中，前面定义的函数会被后定义的同名函数覆盖，也就是说，按上面的场景调用tips 方法最终都调用的都是最后一个。为了明确各个tips所属类，于是就定义了静态方法。


class Car(object):
    pass

    @staticmethod
    def tips():
        print("温馨提示：开车不喝酒")

class Animal(object):
    pass

    @staticmethod
    def tips():
        print("温馨提示：不要伸手投食")

Car.tips()
Animal.tips()
