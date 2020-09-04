# -*- encoding: utf-8 -*-
"""
@File    : 100-迷惑.py
@Time    : 2020/8/22 16:42
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""


class Car(object):  # 类对象
    car_sum = 0  # 类变量，也叫做类属性

    # 构造方法
    def __init__(self, name, price):
        # 实例变量，也叫实例属性
        self.name = name
        self.price = price
        Car.car_sum += 1

    # 实例方法
    def level(self):
        if self.price > 300000:
            print("%s是高档轿车！" % self.name)
        else:
            print("%s是抵挡轿车！" % self.name)

    # 类方法
    @classmethod
    def car_num(cls):
        print("我有%d辆车。" % cls.car_sum)

    # 静态方法
    @staticmethod
    def tips():
        print("喝酒不开车！")

    # 折构方法
    # def __del__(self):
    #     print('对象已删除')

if __name__ == "__main__":
    bmw = Car("宝马", 400000)
    bmw.level()
    bmw.car_num()

