# -*- encoding: utf-8 -*-
"""
@File    : 101-迷惑-汽车-网络.py
@Time    : 2020/8/22 17:10
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

class Car(object):      # 类对象
    car_num = 0   # 类属性，在__init__外部定义。

    #原因：__init__写成了__int__
    def __init__(self, brand, price):
        self.brand = brand  # 实例属性，在__init__内部定义
        self.price = price
        Car.car_num += 1

    def level(self):        # 实例方法，调用了实例属性
        if self.price > 300000:
            print(f"{self.brand}是高级轿车")
        else:
            print(f"{self.brand}是非高级轿车")

    @classmethod
    def car_count(cls):     # 类方法，只访问类变量
        print(f"我有{cls.car_num}辆车")

    @staticmethod
    def tips():     # 静态方法，既不访问成员变量，也不访问类变量
        print("温馨提示：开车不喝酒")

    def __del__(self):
        print('对象已删除')

if __name__ == "__main__":
    bmw = Car("宝马", 200000)     # 通过类创建的对象称为实例对象
    bmw.level()
    wlhg = Car("五菱宏光", 400000)
    wlhg.level()
    Car.car_count()     # 调用类方法
    Car.tips()      # 调用静态方法