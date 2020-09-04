# -*- encoding: utf-8 -*-
"""
@File    : 48-多态.py
@Time    : 2020/8/26 14:10
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    继承、重写状态下的多态
'''
class Car(object):
    def car_name(self):
        print('旧款奥迪车！')

class CarSon(Car):
    def car_name(self):
        print('新款奥迪车！')

def use_car(self):
    self.car_name()

aodi1 = Car()
aodi2 = CarSon()

use_car(aodi1)
use_car(aodi2)

'''
    常见的多态
'''
class AliPay():
    def pay(self, money):
        print("通过支付宝支付%d元" % money)

class ApplePay():
    def pay(self, money):
        print("通过applepay支付%d元" % money)

def pay(pay_obj, money):
    pay_obj.pay(money)

zhifubao = AliPay()
applepay = ApplePay()

pay(zhifubao, 100)
pay(applepay, 200)

