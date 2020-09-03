# -*- encoding: utf-8 -*-
"""
@File    : 46-私有属性和私有方法.py
@Time    : 2020/8/24 11:00
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

class Car(object):

    def __init__(self):
        #私有属性
        self.__age = 4
        #普通属性
        self.age = 10

    #定义一个私有方法，返回私有属性的值
    def __car_age(self):
        return self.__age

    #定义一个实例方法，返回私有属性的值
    def get_car_age_att(self):
        return self.__age

    #定义一个实例方法，调用私有方法，获取私有属性的值
    def get_car_age_met(self):
        return self.__car_age()

    #修改私有属性的值
    def set_car_name(self):
        self.__age = 5

bmw = Car()

print('直接获取实例属性的值：%d' % bmw.age)#方法外，可以获取实例属性的值
# print(bmw.__age)#方法外，无法获取私有属性的值

print('通过调用实例方法，获取私有属性的值：%d' % bmw.get_car_age_att())#方法外，可以调用实例方法
# print(bmw.__car_age())#方法外，无法调用私有方法

#调用修改私有属性的值的方法
bmw.set_car_name()

#调用调用私有方法的实例方法，获取私有属性的值
print('调用调用私有方法的实例方法，获取私有属性的值：%d' % bmw.get_car_age_met())



