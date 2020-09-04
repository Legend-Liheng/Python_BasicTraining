# -*- encoding: utf-8 -*-
"""
@File    : 44-类和对象（实例属性和实例方法）.py
@Time    : 2020/8/26 15:08
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

#定义一个类
class Car():

    #实例方法
    def name(self, name):

        #实例属性
        self.name = name
        print('这是个%s车' % self.name)

#对象：对类进行实例化
bmw = Car()
print(bmw.name)

#实例调用实例方法
bmw.name('宝马')

#使用实例属性：对象名.实例属性名
print(bmw.name)

